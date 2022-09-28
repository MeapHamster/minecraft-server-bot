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

        if function == "add":
            embed = discord.Embed(
                title = 'Attempting to add user to whitelist',
                colour = discord.Colour.dark_grey()
            )
            await interaction.response.send_message(embed = embed)
            print("Adding user to whitelist")
            pyautogui.write('whitelist add' + username, interval = .1)
            pyautogui.press('enter')
            await interaction.edit_original_response(embed = discord.Embed(
                title = 'User added to whitelist',
                colour = discord.Colour.dark_grey()
            ))
        else:
            embed = discord.Embed(
                title = 'Attempting to remove user from whitelist',
                colour = discord.Colour.dark_grey()
            )
            await interaction.response.send_message(embed = embed)
            print("Removing user from whitelist")
            pyautogui.write('whitelist remove' + username, interval = .1)
            pyautogui.press('enter')
            time.sleep(1)
            await interaction.edit_original_response(embed = discord.Embed(
                title = 'User removed from whitelist',
                colour = discord.Colour.dark_grey()
            ))

    else:
        
        await interaction.response.send_message(content = 'You do not have permission to use this command', ephemeral = True)