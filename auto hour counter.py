import discord
from discord.ext import commands

import time
from time import sleep

token = input('TOKEN: ')
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"))

@client.event
async def on_ready():
    print("Type \"start\" to start the counter. Posts hour exactly every hour.")

@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        if message.content.startswith('start'):
            for i in range(1, 100):
                time.sleep(3600)
                await message.channel.send(f"Hour {i}")
        
client.run(token, bot=False)