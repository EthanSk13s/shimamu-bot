import itertools

import discord
import aiohttp
from discord.ext import commands
from functools import partial

try:
    from .utils import misc
except (SystemError, ImportError):
    import misc

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

    @commands.command()
    async def wal(self, ctx, link=None):
        async with ctx.typing():
            if link is None:
                attachment = ctx.message.attachments[0].url
            else:
                attachment = link

            async with self.bot.session.get(attachment) as c:
                image = await c.read()

                fn = partial(misc.generate, image)

                buffer = await self.bot.loop.run_in_executor(None, fn)

                file = discord.File(filename="rgb.png", fp=buffer)

                await ctx.send(file=file)

def setup(bot):
    bot.add_cog(Info(bot))