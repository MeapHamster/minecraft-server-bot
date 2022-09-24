import discord
import pyautogui
import time

async def cmd_RunServer_Invoked(Member, interaction):

    if Member.guild_permissions.administrator == True:

        time.sleep(1)

        print("Stopping Server...")

        pyautogui.write('stop', interval = .1)
        
        print("Server Terminated")

        pyautogui.write('a', interval = .1)

        await interaction.response.send_message(content = 'Server stopped', ephemeral = False)

    else:
        
        await interaction.response.send_message(content = 'You do not have permission to use this command', ephemeral = True)