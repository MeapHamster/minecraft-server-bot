import discord
# from subprocess import Popen
import time
import os

async def cmd_RunServer_Invoked(Member, interaction):

    if Member.guild_permissions.administrator == True:

        ## Run the server here idk how to do it yet

        # p = Popen(r"C:\Users\Fayas\Desktop\Minecraft_Server\\run.bat", shell=True, stdout = subprocess.PIPE)
        # stdout, stderr = p.communicate()

        # subprocess.call(["C:\\Users\\Fayas\\Desktop\\Minecraft_Server\\run.bat"])

        embed_1 = discord.Embed(
            title = 'Sending Request to Start...',
            colour = discord.Colour.dark_grey()
        )
        embed_2 = discord.Embed(
            title = 'Server Online',
            colour = discord.Colour.dark_grey()
        )

        remainingTime = 60

        # await interaction.response.send_message(content = 'Running server...')
        await interaction.response.send_message(embed = embed_1)

        os.chdir(r"C:\Users\Fayas\Desktop\Minecraft_Server")
        os.startfile("run.bat")

        time.sleep(5)
        
        for i in range(remainingTime, 0, -10):
            embed = discord.Embed(
                title = 'Starting Server...',
                description = str(i) + ' seconds remaining...',
                colour = discord.Colour.dark_grey()
            )
            await interaction.edit_original_response(embed = embed)

            time.sleep(10)
        
        await interaction.edit_original_response(embed = embed_2)


    else:
        
        await interaction.response.send_message(content = 'You do not have permission to use this command', ephemeral = True)