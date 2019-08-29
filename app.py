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
        embed.add_field(name="commands:", value="for list of commands visit: http://rabbit001.cf/commands.html", inline=False)
        embed.add_field(name="U want invite my bot to ur server? Use this link:", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.channel.send(message.channel, embed=embed)

        
client.run(os.getenv('BOT_TOKEN'))
