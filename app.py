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


        #you can change the prefix to what you want, just keep it inside the quotations
bot =commands.Bot(command_prefix ="!")

@bot.event
async def on_ready():
    #what the terminal say when the bot goes online
    print("Anti-Spam Bot is Online!, running version " + discord.__version__ + " of Discord.py")
    await asyncio.sleep(10)
    #this sets what tame the bot is playing
    await bot.change_presence(game=discord.Game(name="This server", type=3))

@bot.command()
async def ping():
    await bot.say("pong!")
    
@bot.command(pass_context = True)
async def spam(ctx)
    if ctx.message.author.permissions_in(ctx.message.channel).manage_server== True:
        await bot.say("This channel is now closed - if you message this channel and you dont have a role, you will  be muted")
        waitmsg = await self.bot.wait_for_message(channel=ctx.message.channel, author = ctx.message.author)
        async def on_message(message):
            #do shit about muting people
            #do a wait_for_message
        if waitmsg.content.lower() == "!spam stop":
            return
        
client.run(os.getenv('BOT_TOKEN'))
