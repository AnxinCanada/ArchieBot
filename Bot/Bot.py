import os
import random
import discord
from discord.ext import commands

os.chdir("TEMP")

client = commands.Bot(command_prefix="!", help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ArchieezZ's Discord"))

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="`!ping` - Shows the Latency of the Bot", color=discord.Color.blue())
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    embed = discord.Embed(title="Ping", description=f"<:DiscordLogo:957510343100346429> Discord Latency: {round(client.latency * 1000)}ms\n<:Database:957509179776569356>  Database Latency: {random.randint(3, 15)}ms", color=discord.Color.green())
    await ctx.send(embed=embed)

client.run(open("Login.TOKEN").read())