import discord
from discord.ext import commands
import asyncio
import time
import random
from discord import Game
import os

Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        embed = discord.Embed(title="For more info visit http://rabbit001.cf", description="", color=0x00ff00)
        embed.add_field(name="Fiel1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(message.channel, embed=embed)

        
client.run(os.getenv('BOT_TOKEN'))
