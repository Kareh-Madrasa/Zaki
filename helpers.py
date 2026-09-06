from groq import AsyncGroq as Groq
import asyncio
import aiosqlite

from _settings import *
import datetime
import discord

client = Groq(
    api_key=GROQ_API_KEY,
)

async def fetch_models():
    models = await client.models.list()

    for model in models.data:
        print(model.id)

async def save_memory(message:discord.Message):
    async with aiosqlite.connect('db.memory') as cur:
        await cur.execute("CREATE TABLE IF NOT EXISTS memory(username, channel_name, date, server_name, your_response)")
        await cur.execute("INSERT INTO memory VALUES (?, ?, ?, ?, ?)")

async def generate_text(message:discord.Message):
    """Generates text using Groq. Automatically handles the bot's contextual memory instead of the older versions where you had to manually manage it [COMING SOON]

    Args:
        message (discord.Message): the message arg in the on_message(message) listener

    Returns:
        str: the Groq resposne
    """
    chat_completion = await client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_instructions}, 
            {"role": "user", "content": f"Context: message sender name: {message.author.display_name}, channel name: {message.channel.name}, server name: {message.guild.name}, Message: {message.content}"}
        ]
    )
    return chat_completion.choices[0].message.content
    
async def isDebugModeOn():
    return debug_mode

async def log_info(msg):
    print(f"[DATE] {datetime.datetime.now(datetime.timezone.utc)} [INFO] {msg}")

async def log_debug(msg):
    print(f"[DATE] {datetime.datetime.now(datetime.timezone.utc)} [DEBUG] {msg}")

async def log_warn(msg):
    print(f"[DATE] {datetime.datetime.now(datetime.timezone.utc)} [WARNING] {msg}")

async def log_error(msg):
    print(f"[DATE] {datetime.datetime.now(datetime.timezone.utc)} [ERROR] {msg}")

# ENTRY POINT
async def main():
    while True:
        try:
            text = input("You: ")
            print(await generate_text(text))
        except Exception as e:
            print(f"Unhandled error: {e}")
            await fetch_models()

if __name__ == "__main__":
    asyncio.run(main())