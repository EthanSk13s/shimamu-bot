import itertools

import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def server(self, ctx):
        guild = ctx.guild

        embed=discord.Embed(title=guild.name, description=f'Members: {len(guild.members)}',
        color=0xd629c9)

        embed.set_author(name=f'Owner: {guild.owner.name}',
        icon_url=guild.owner.avatar_url)

        embed.set_thumbnail(url=guild.icon_url)

        embed.add_field(name='Number of Channels:', value=len(guild.channels))
        embed.add_field(name='Region', value=guild.region)
        embed.add_field(name='Time of Creation', value=guild.created_at)

        await ctx.send(embed=embed)

    @commands.command()
    async def pfp(self, ctx, *, user: str = None):
        member = user or ctx.author.name

        h = await commands.UserConverter().convert(ctx, member)
        avatar_url = h.avatar_url_as(format="png")

        await ctx.send(avatar_url)

def setup(bot):
    bot.add_cog(Info(bot))