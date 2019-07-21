import itertools

import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def server(self, ctx):
        guild = ctx.guild

        embed=discord.Embed(title=guild.name, description=f'Members: {len(guild.members)}')
        embed.add_field(name='Number of Channels:', value=len(guild.channels))

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))