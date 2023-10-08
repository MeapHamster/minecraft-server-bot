import discord
import pyautogui
import time

import edit_settings

async def cmd_Whitelist_Invoked(Member, interaction, function, username):

    if Member.guild_permissions.administrator == True:

        if edit_settings.getServerStatus() == False:
            response_embed = discord.Embed(
                title = 'Server is offline',
                description = 'Use </runserver:0> to start the server',
                colour = discord.Colour.dark_grey()
            )
            await interaction.response.send_message(embed = response_embed)
            return

        embed = discord.Embed(
            title = 'Setting weather to ' + function,
            colour = discord.Colour.dark_grey()
        )
        await interaction.response.send_message(embed = embed)
        print("Setting weather to " + function)
        pyautogui.write('weather ' + function, interval = .1)
        pyautogui.press('enter')
        await interaction.edit_original_response(embed = discord.Embed(
            title = 'Set weather to ' + function,
            colour = discord.Colour.dark_grey()
        ))

    else:
        
        await interaction.response.send_message(content = 'You do not have permission to use this command', ephemeral = True)