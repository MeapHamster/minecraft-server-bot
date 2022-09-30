import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

from Modules.Whitelist import cmd_Whitelist_Invoked

class whitelist(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = 'whitelist',
        description = 'Add or remove a user from the whitelist!'
    )

    @app_commands.describe(
        function = "How are you editing the whitelist?",
        username = "Who would you like to edit whitelist permissions for?"
    )

    @app_commands.choices(
        function = [
            Choice(name = 'add', value = 'add'),
            Choice(name = 'remove', value = 'remove'),
        ],
    )

    async def whitelist(
        self,
        interaction: discord.Interaction,
        function: str,
        username: str,
        ) -> None:

        await cmd_Whitelist_Invoked(interaction.user, interaction, function, username)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        whitelist(bot),
    )