# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@bot.command(name='register', help='Start user registration')
async def on_message(ctx):
    user = ctx.message.author
    channel = await user.create_dm()
    roles = []
    for i in user.roles:
        roles.append(i.name)
    response = f'Starting user registration for user {user.id} with roles {roles}'
    await channel.send(response)


bot.run(TOKEN)
