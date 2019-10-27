import aiowiki
import discord
from discord.ext import commands

# pylint throws an error if I do not include this try statement it's dumb...

try:
	from .utils import scrape
except (SystemError, ImportError):
	import scrape

class Chara():
    def __init__(self, values: dict):
        self.name = values['name']
        self.desc = values['desc']
        self.skills = values['skills']
        self.image = values['image']
        self.element = values['element']
        self.hp = values['hp']
        self.atk = values['atk']

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

        summary = scrape.summary(url)

        await ctx.send(summary)

def setup(bot):
    bot.add_cog(GBF(bot))