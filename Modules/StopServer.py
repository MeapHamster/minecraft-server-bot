import discord
import pyautogui
import time

import edit_settings

async def cmd_StopServer_Invoked(Member, interaction):

    if Member.guild_permissions.administrator == True:

        # if edit_settings.getRunning() == True:
        #     response_embed = discord.Embed(
        #         title = 'Command running',
        #         description = 'Please wait for the command to finish executing',
        #         colour = discord.Colour.dark_grey()
        #     )
        #     await interaction.response.send_message(embed = response_embed)
        #     return

        if edit_settings.getServerStatus() == False:
            response_embed = discord.Embed(
                title = 'Server is offline',
                description = 'Use </runserver:0> to start the server',
                colour = discord.Colour.dark_grey()
            )
            await interaction.response.send_message(embed = response_embed)
            return

        edit_settings.setRunning()
        edit_settings.setOffline()

        print("Stopping Server")

        embed_1 = discord.Embed(
            title = 'Sending Request to Terminate...',
            colour = discord.Colour.dark_grey()
        )
        embed_2 = discord.Embed(
            title = 'Terminating Server...',
            colour = discord.Colour.dark_grey()
        )
        embed_3 = discord.Embed(
            title = 'Server Offline',
            colour = discord.Colour.dark_grey()
        )

        # await interaction.response.send_message(content = 'Sending Request to Terminate...')
        await interaction.response.send_message(embed = embed_1)

        print("Stopping Server...")

        pyautogui.write('stop', interval = .1)
        pyautogui.press('enter')
        
        print("Server Terminated")

        time.sleep(4)

        # interactionResponse = await interaction.original_message()

        # await interaction.edit_original_response(content = "Terminating Server...")
        await interaction.edit_original_response(embed = embed_2)

        time.sleep(4)

        pyautogui.write('a', interval = .1)

        # await interaction.edit_original_response(content = "Successfully Terminated Server")
        await interaction.edit_original_response(embed = embed_3)

        edit_settings.setWaiting()

    else:
        
        await interaction.response.send_message(content = 'You do not have permission to use this command', ephemeral = True)