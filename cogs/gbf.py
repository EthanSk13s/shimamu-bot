import aiowiki
import discord
from discord.ext import commands

# pylint throws an error if I do not include this try statement it's dumb...

try:
	from .utils import scrape
except (SystemError, ImportError):
	import scrape

class GBF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.diffs = {
            'normal': '#Normal',
            'hard': '#Hard',
            'hard+': '#Hard.2B',
            'extreme': '#Extreme',
            'extreme+': '#Extreme.2B',
            'impossible': '#Impossible',
            'impossible (hard)': '#Impossible_.28Hard.29'
        }

    @commands.group()
    async def gbf(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("No subcommand passed!")

    @gbf.command()
    async def chara(self, ctx, *, query):
        wiki = aiowiki.Wiki("https://gbf.wiki/api.php")
        pages = await wiki.opensearch(query)
        url = await pages[0].html()

        char = scrape.CharaScraper(url)

        embed = discord.Embed(title=f'{char.title()} {char.name()}',
        description=char.summary())
        embed.set_image(url=char.image())
        embed.set_thumbnail(url=char.element())

        embed.add_field(name='Max HP', value=char.hp())
        embed.add_field(name='Max ATK', value=char.atk())
        embed.add_field(name='Skills',
        value=f"\n".join(char.skills()))

        await ctx.send(embed=embed)
        await wiki.close()

    @gbf.command()
    async def raid(self, ctx, query, difficulty):
        wiki = aiowiki.Wiki("https://gbf.wiki/api.php")
        pages = await wiki.opensearch(query)
        url = None

        for page in pages:
            if 'raid' in page.title.lower():
                url = await page.html()
                break

        raid = scrape.RaidScraper(url, difficulty)
        embed = discord.Embed(title=raid.name())
        embed.set_thumbnail(url=raid.image())

        embed.add_field(name="Required AP:", value=raid.cost())
        embed.add_field(name="Requirements:", value=raid.unlock())
        embed.add_field(name="Location:", value=raid.location())

        await ctx.send(embed=embed)
        await wiki.close() 

def setup(bot):
    bot.add_cog(GBF(bot))