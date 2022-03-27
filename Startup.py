import os
import sys
import discord
from discord.ext import commands

Client = commands.Bot(command_prefix="!", help_command=None)

@Client.command()
async def reboot(ctx):
        await Client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="SERVER REBOOT"))
        try:
            os.system("mv 'TEMP/assets' 'assets'")
        except Exception:
            pass
        os.system("svn checkout https://github.com/AnxinCanada/ArchieBot/trunk/Bot TEMP")
        try:
            os.system("mv assets TEMP/assets")
        except Exception:
            pass
        try:
            os.system("cp Bot/Login.TOKEN TEMP/Login.TOKEN")
        except Exception:
            pass
        os.system("python3 Runtime.py")
        sys.exit(0)

@Client.event
async def on_ready():
    os.system("python3 TEMP/Bot.py")

Client.run(open("Bot/Login.TOKEN").read())