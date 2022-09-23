import discord
import typing
from discord import app_commands
from discord.ext import commands

from Modules.RunServer import cmd_RunServer_Invoked

class runserver(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = 'runserver',
        description = 'Run the Minecraft server!'
    )

    async def profile(
        self,
        interaction: discord.Interaction,
        ) -> None:

        await cmd_RunServer_Invoked(interaction.user, interaction)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        profile(bot),
    )