import os

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
SERVER_ID = os.getenv('DISCORD_SERVER_ID')

baseURL = "https://kaal-backend.herokuapp.com/"

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.command(name='register', help='Start user registration')
async def on_message(ctx):
    user = ctx.message.author
    channel = await user.create_dm()
    roles = []
    for i in user.roles:
        roles.append(i.name)

    r = requests.post(
        url=baseURL + '/register/',
        json={"userId": str(user.id), "userName": str(user), "roles": roles},
    )

    res = r.json()
    print(res)
    userHash = res['userHash']
    resp2 = f'Your key is: {userHash}. Please enter it in the CLI'
    await channel.send(resp2)
    response = f'Starting user registration for user {user.id} with roles {user.roles}'
    await channel.send(response)

    # Code for creating webhooks for each channel

    # Get all text_channels grouped by categories
    category_dict = dict(ctx.guild.by_category())

    # Store categories and channels user has access to

    available_categories = []
    available_channels = []

    # Match category name according to name of the role which user have
    for role in user.roles:
        for category in ctx.guild.categories:
            if role.name in category.name:
                # If the name of a role of user is present in name of a
                # category, then store such category
                available_categories.append(category)

    # For each matched category, store channel in that category
    # which are named 'general'
    # TODO: make channel lookup name configurable by user
    for category in available_categories:
        for channel in category_dict[category]:
            if channel.name == 'general':
                available_channels.append(channel)

    # TODO: Check in database, whether a webhook has been already created for these channel

    # Create webhooks for all channels in "available channel"
    for channel in available_channels:
        # TODO: Remove this when lookup for database is implemented
        available_webhooks = await channel.webhooks()
        webhook_exists = False
        for webhook in available_webhooks:
            if webhook.name == 'moropy_bot':
                webhook_exists = True
        if not webhook_exists:
            webhook = await channel.create_webhook(name='moropy_bot')

    # TODO: Update the link of this webhook to the database.

bot.run(TOKEN)
