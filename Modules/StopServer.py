import discord
import pyautogui
import time

async def cmd_StopServer_Invoked(Member, interaction):

    if Member.guild_permissions.administrator == True:

        embed_1 = discord.Embed(
            title = 'Sending Request to Terminate...',
            colour = discord.Colour.dark_grey()
        )
        embed_2 = discord.Embed(
            title = 'Terminating Server...',
            colour = discord.Colour.dark_grey()
        )
        embed_3 = discord.Embed(
            title = 'Successfully Terminated Server',
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

    else:
        
        await interaction.response.send_message(content = 'You do not have permission to use this command', ephemeral = True)