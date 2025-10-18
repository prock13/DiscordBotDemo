from dotenv import load_dotenv
import discord
import os

load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')

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

client.run(DISCORD_TOKEN)
