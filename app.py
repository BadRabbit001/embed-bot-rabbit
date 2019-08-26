import discord
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        embed = discord.Embed(title="Tile", description="Desc", color=0x00ff00)
        await message.channel.send(message.channel, embed=embed)
        
client.run(NTk4NTM2MTQ0NTg5OTQ2ODg1.XWP3Ng.eZNdKeRP69cq4RgDMQs2HCyAstg)
