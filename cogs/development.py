import traceback
import sys

import discord
from discord.ext import commands

class Development(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def presence(self, ctx, *, text):
        await self.bot.change_presence(activity=discord.Game(text))
        await ctx.send(f'Presence Changed to: {text}')

    @commands.group(hidden=True)
    @commands.is_owner()
    async def cog(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('No Subcommand passed!')

    @cog.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, cog):
        try:
            self.bot.unload_extension(f'cogs.{cog}')
            self.bot.load_extension(f'cogs.{cog}')
            await ctx.send(f'{cog} has been reloaded!')
        except Exception as e:
            error = f'{type(e).__name__} - {e}'
            await ctx.send(f'{cog} failed to reload\n```py\n{error}\n```')

    @cog.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, cog):
        try:
            self.bot.load_extension(f'cogs.{cog}')
            await ctx.send(f'{cog} is now loaded')
        except Exception as e:
            error = f'{type(e).__name__ - e}'
            await ctx.send(f'{cog} failed to load\n```py\n{error}\n```')

def setup(bot):
    bot.add_cog(Development(bot))