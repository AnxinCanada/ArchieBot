import os
import discord
from discord.ext import commands

os.chdir("TEMP")

client = commands.Bot(command_prefix="!", help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ArchieezZ's Discord"))

client.run(open("Login.TOKEN").read())