import os
import discord
import subprocess
from discord.ext import commands

Client = commands.Bot(command_prefix="!", help_command=None)

@Client.command(aliases=["reboot", "restart"])
async def update(ctx):
    works = 0
    try:
        if ctx.author.id == 746446670228619414:
            works = 1
    except Exception:
        works = 0
    if works:
        try:
            p.terminate()
        except Exception:
            pass
        await Client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="SERVER REBOOT"))
        try:
            os.system("mv TEMP/assets assets")
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
        p = subprocess.Popen(['python', 'TEMP/Bot.py'])

@Client.event
async def on_ready():
    await update(Client.get_guild(957246253157191711).get_channel(957258191459213322))

Client.run(open("Bot/Login.TOKEN").read())