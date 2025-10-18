from dotenv import load_dotenv
from openai import OpenAI
import discord
import os

load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

oa_client = OpenAI(api_key=OPENAI_KEY)

# ask openai a question
async def call_openai(question):
    response = oa_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", 
            "content": f"You are a helpful assistant. Answer the following question concisely.\n\nQuestion: {question}",
            },
        ]
    )
    response = response.choices[0].message.content
    print(f"OpenAI response: {response}")
    return response

# Setup intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        await message.channel.send('How can I assist you today?')

    if message.content.startswith('$question'):
        print(f"Message: {message.content}")
        message_content = message.content.split("$question")[1]
        print(f"Question: {message_content}")
        response = await call_openai(message_content)
        print(f"Sending response: {response}")
        print("---")
        await message.channel.send(response)

client.run(DISCORD_TOKEN)