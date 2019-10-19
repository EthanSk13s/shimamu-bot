import discord
import asyncKirara
from discord.ext import commands

import config

extensions = {
    'cogs.deresute',
    'cogs.development',
    'cogs.info',
    'cogs.anime',
    'cogs.music'
}
class ShimamuBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix='u!', description="Ganbarimasu!")
        self.attributes = {
            'cute': 0xd629c9,
            'cool': 0x4907f8,
            'passion': 0xf2a80d
        }

        for extension in extensions:
            try:
                self.load_extension(extension)
            except:
                print('load fail')

    async def on_ready(self):
        print('Ganbarimasu!')

    def run(self):
        super().run(config.token, reconnect=True)

bot = ShimamuBot()
bot.run()