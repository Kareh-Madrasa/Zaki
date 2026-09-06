import discord
from discord.ext import commands
import asyncio

from _settings import *
from helpers import *

client = commands.AutoShardedBot(command_prefix="bro", intents=discord.Intents.all())

async def main():
    @client.event
    async def on_ready():
        await log_info(f"Logged in as {client.user.name} (ID: {client.user.id})")
        
    @client.event
    async def on_message(message:discord.Message):
        if message.author == client.user:
            await log_debug("Is client.user, skipping.") if isDebugModeOn() else None
            return

        # lets be honest, you wouldnt call anyone on discord by their username, you'd call them by their display name
        await log_debug("Responding...") if isDebugModeOn() else None

        if client.user in message.mentions:
            async with message.channel.typing():
                context = f"name: {message.author.display_name}, channel name: {message.channel.name}, server name: {message.guild.name}, current time: {datetime.datetime.now(datetime.UTC)}"

                await message.reply(await generate_text(message=message))
    await log_info("Starting the bot...")
    await client.start(BOT_TOKEN, reconnect=True)
    
asyncio.run(main())