import discord
import requests
import secrets
import subprocess

async def cmd_RunServer_Invoked(Member, interaction):

    if Member.guild_permissions.administrator == True:

        ## Run the server here idk how to do it yet
        subprocess.call(['path to file.bat'])

    else:
        
        await interaction.response.send_message(content = 'You do not have permission to use this command', ephemeral = True)