# bot.py
import os

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

<<<<<<< HEAD
baseURL = "https://kaal-backend.herokuapp.com/"
=======
baseURL = os.getenv('BASEURL')
>>>>>>> 0eeee1a5d69f3a9c3fad2e7dd985b91bab7ee414

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.command(name='register', help='Start user registration')
async def on_message(ctx):
    user = ctx.message.author
    channel = await user.create_dm()
    roles = []
    for i in user.roles:
        roles.append(i.name)
<<<<<<< HEAD

    response = (
        f'Starting user registration for {user}. Please check your DM to receive your user key'
    )

    await ctx.send(response)
=======
    response = (
        f'Starting user registration for user {user} with roles {roles}, please wait...'
    )
    await channel.send(response)
>>>>>>> 0eeee1a5d69f3a9c3fad2e7dd985b91bab7ee414
    r = requests.post(
        url=baseURL + '/register/',
        json={"userId": str(user.id), "userName": str(user), "roles": roles},
    )

    res = r.json()
<<<<<<< HEAD
    print(res)
=======
>>>>>>> 0eeee1a5d69f3a9c3fad2e7dd985b91bab7ee414
    userHash = res['userHash']
    resp2 = f'Your key is: {userHash}. Please enter it in the CLI'
    await channel.send(resp2)


bot.run(TOKEN)
