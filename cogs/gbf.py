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

    @commands.group()
    async def gbf(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("No subcommand passed!")

    @gbf.command()
    async def chara(self, ctx, *, query):
        wiki = aiowiki.Wiki("https://gbf.wiki/api.php")
        page = wiki.get_page(query)
        url = await page.html()

        char = scrape.CharaScraper(url)
        embed = discord.Embed(title=f'{char.title()} {char.name()}',
        description=char.summary())
        embed.set_image(url=char.image())
        print(char.title())

        await ctx.send(embed=embed)
        await wiki.close()

def setup(bot):
    bot.add_cog(GBF(bot))