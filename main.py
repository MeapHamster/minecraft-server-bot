import discord
from discord.ext import commands, tasks

import settings
settings.init()

token = 'MTAyMjY5ODQ5OTI5NDM2NzgxNQ.GOJIfZ.Iqo8Bye8IXZbgTtV7SikSB3-SnYLEdQriogbnc'

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = ':',
            intents = discord.Intents.all(),
            application_id = 1022698499294367815
        )

        @self.command(name = 'testConnect')
        async def productpurchase(ctx, arg):
            print('Invoked')

        self.initial_extentions = [
            'cogs.runserver',
            'cogs.stopserver',
        ]

    async def setup_hook(self):
        for ext in self.initial_extentions:
            await self.load_extension(ext)
            print('Loaded ' + ext)

        await bot.tree.sync()
    
    async def on_ready(self):
        print(f'{self.user} has connected to Discord')

bot = MyBot()
bot.run(token)