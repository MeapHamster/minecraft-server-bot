import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

from Modules.Weather import cmd_Weather_Invoked

class weather(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = 'weather',
        description = 'Set the weather!'
    )

    @app_commands.describe(
        function = "What do you want to set the weather to?",
    )

    @app_commands.choices(
        weather_type = [
            Choice(name = 'clear', value = 'clear'),
            Choice(name = 'rain', value = 'rain'),
            Choice(name = 'thunder', value = 'thunder'),
        ],
    )

    async def weather(
        self,
        interaction: discord.Interaction,
        weather_type: str,
        ) -> None:

        await cmd_Weather_Invoked(interaction.user, interaction, function, username)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        weather(bot),
    )