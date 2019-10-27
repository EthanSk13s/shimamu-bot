import discord
import aiowiki
import bs4 as bs

from discord.ext import commands
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

        soup = bs.BeautifulSoup(url, 'lxml')
        desc = soup.find('table', 
        {'class':'wikitable',
        'style': 'width:100%; text-align:center; text-size-adjust: none; margin-top:0;'}
        )
        pog = str(desc.find_all('td'))
        thing = pog.strip('[').strip(']').strip('<td>').strip('</td>')

        await ctx.send(thing)

def setup(bot):
    bot.add_cog(GBF(bot))