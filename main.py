import discord
from discord.ext import commands
import asyncio

from _settings import *
from helpers import *

client = commands.AutoShardedBot(command_prefix="bro", intents=discord.Intents.all())

async def main():
    @client.event
    async def on_ready():
        log_info(f"Logged in as {client.user.name} (ID: {client.user.id})")

    @client.event
    async def on_mesage(message:discord.Message):
        if message.author == client.user:
            return
        
    await client.start(BOT_TOKEN, reconnect=True)

asyncio.run(main())