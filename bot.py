import discord
from discord.ext import commands
from random import *

TOKEN = 'token'

client = discord.Client()
description = '''ninjaBot in Python'''
bot = commands.Bot(command_prefix='?', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")


@bot.command()
async def zepek():
    """Says world"""
    await bot.say("cokolada>vanilija")


@bot.command()
async def add(left: float, right: float):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def sub(left: float, right : float):
    """Subtracts two numbers."""
    await bot.say(left - right)


@bot.command()
async def txt(wrd: str):
    """Texts the word"""
    await bot.say(wrd)


@bot.command()
async def rnum():
    """Displays a random number"""
    r = randint(0, 100)
    await bot.say(r)


bot.run(TOKEN)
