import discord
from discord import app_commands
from discord.ext import commands

from Modules.StopServer import cmd_StopServer_Invoked

class stopserver(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = 'stopserver',
        description = 'Stop the Minecraft server!'
    )

    async def stopserver(
        self,
        interaction: discord.Interaction,
        ) -> None:

        await cmd_StopServer_Invoked(interaction.user, interaction)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        stopserver(bot),
    )