import discord
# from subprocess import Popen
import os

async def cmd_RunServer_Invoked(Member, interaction):

    if Member.guild_permissions.administrator == True:

        ## Run the server here idk how to do it yet

        # p = Popen(r"C:\Users\Fayas\Desktop\Minecraft_Server\\run.bat", shell=True, stdout = subprocess.PIPE)
        # stdout, stderr = p.communicate()

        # subprocess.call(["C:\\Users\\Fayas\\Desktop\\Minecraft_Server\\run.bat"])

        os.chdir(r"C:\Users\Fayas\Desktop\Minecraft_Server")
        os.startfile("run.bat")

        await interaction.response.send_message(content = 'Running server...', ephemeral = False)

    else:
        
        await interaction.response.send_message(content = 'You do not have permission to use this command', ephemeral = True)