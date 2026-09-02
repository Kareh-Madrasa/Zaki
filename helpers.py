from groq import AsyncGroq as Groq
import asyncio
import aiosqlite

from _settings import *
import datetime

client = Groq(
    api_key=GROQ_API_KEY,
)

async def fetch_models():
    models = await client.models.list()

    for model in models.data:
        print(model.id)

async def generate_text(text:str):
    chat_completion = await client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": "Hello"}
        ]
    )
    return chat_completion.choices[0].message.content

def log_info(msg):
    print(f"[DATE] {datetime.datetime.now(datetime.timezone.utc)} [INFO] {msg}")

def log_debug(msg):
    print(f"[DATE] {datetime.datetime.now(datetime.timezone.utc)} [DEBUG] {msg}")

def log_warn(msg):
    print(f"[DATE] {datetime.datetime.now(datetime.timezone.utc)} [WARNING] {msg}")

def log_error(msg):
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