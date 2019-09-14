import discord
import aiohttp

from discord.ext import commands

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.path = 'https://kitsu.io/api/edge/'

    @commands.command()
    async def anime(self, ctx, *, anime):
        async with aiohttp.ClientSession() as s:
            async with s.get(f"{self.path}anime?filter[text]={anime}") as r:
                response = await r.json()

        embed = discord.Embed(title=response['data'][0]['attributes']['canonicalTitle'],
        description=response['data'][0]['attributes']['synopsis'])
        embed.set_thumbnail(url=response['data'][0]['attributes']['posterImage']['large'])

        await ctx.send(embed=embed)

    @commands.command()
    async def manga(self, ctx, *, manga):
        async with aiohttp.ClientSession() as s:
            async with s.get(f"{self.path}manga?filter[text]={manga}") as r:
                response = await r.json()

        embed = discord.Embed(title=response['data'][0]['attributes']['canonicalTitle'],
        description=response['data'][0]['attributes']['synopsis'])
        embed.set_thumbnail(url=response['data'][0]['attributes']['posterImage']['large'])

        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Anime(bot))            
    