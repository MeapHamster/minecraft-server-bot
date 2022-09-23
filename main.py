
import discord
from discord.ext import commands, tasks
from Utilities.HandlePurchaseCheck import *

token = ''

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = ':',
            intents = discord.Intents.all(),
            application_id = 906639102558994442
        )

        @self.command(name = 'testConnect')
        async def productpurchase(ctx, arg):
            print('Invoked')

        self.initial_extentions = [
            'cogs.runserver',
        ]

    async def setup_hook(self):
        for ext in self.initial_extentions:
            await self.load_extension(ext)
            print('Loaded ' + ext)

        await bot.tree.sync()

        self.CheckPurchases.start()
    
    async def on_ready(self):
        print(f'{self.user} has connected to Discord')

bot = MyBot()
bot.run(token)