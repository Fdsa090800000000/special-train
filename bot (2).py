import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} 已上線")

@bot.command()
async def ping(ctx):
    await ctx.send("機器人正常運作!")

bot.run("MTQ2NTY3ODM1MzgyNTY2NTE1Nw.GjsWwe.zy2QRKc2tUZLTgeLQEg3e1I7aJ8CJlbf4v6D5I")