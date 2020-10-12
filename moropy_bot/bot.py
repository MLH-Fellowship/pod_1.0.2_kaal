import discord
import utils
from discord.ext import commands

from . import config

client = discord.Client()
bot = commands.Bot(command_prefix='!')

CHANNEL_WEBHOOK_URL = {}


@bot.command(name='register', help='Start user registration')
async def on_message(ctx):
    user = ctx.message.author

    # Send acknowledgement to user on current channel
    current_channel = ctx.message.channel
    await current_channel.send(
        f'<@{user.id}> we have started registration for you, '
        'keep an eye on your DMs for further instructions. :wink:'
    )

    user_dm = await user.create_dm()
    user_roles = [role.name for role in user.roles]

    # Check whether the user has already registered
    user_exists, userHash = utils.validate_user(user.id)
    if user_exists:
        await current_channel.send(
            f'We have met before <@{user.id}>! I have sent you a present on DM :smiling_imp:'
        )
        await user_dm.send(
            f'There you go with you hashCode: `{userHash}`. '
            'You can now register yourself through the CLI.'
            f'When in doubt, head over to our documentation: {config.DOCUMENTATION_URL}'
        )
        return

    # Send greetings to user on DM
    await user_dm.send(config.LOADING_GIF_URL)
    await user_dm.send(
        f'<@{user.id}> we have started moving things for you! Meanwhile, you '
        'can have a look at our documentation: '
    )

    # Register user on Kaal Backend
    status_code, userHash = utils.registerUser(user.id, user.name, user_roles)

    if userHash:
        await user_dm.send(config.BOOM_GIF_URL)
        await user_dm.send(
            f'Kudos <@{user.id}>! There you go with you hashCode: `{userHash}`. '
            'You can now register yourself through the CLI.'
            'When in doubt, head over to our documentation: '
        )
    else:
        await user_dm.send(
            'Oh no! It seems like we are currently facing a problem registering '
            'you in our database, please report your bug report on our GitHub, '
            f'with this code `{status_code}`. Our developers will help you!'
        )

    await create_webhooks_for_users(ctx, user, userHash)


async def create_webhooks_for_users(ctx, user, userHash):
    # Code for creating webhooks for each channel
    # Get all text_channels grouped by categories
    category_dict = dict(ctx.guild.by_category())

    # Store categories and channels user has access to
    user_categories = []
    user_channels = []
    user_webhooks = []

    # Match category name according to name of the role which user have
    for role in user.roles:
        for category in ctx.guild.categories:
            if role.name in category.name:
                # If the name of a role of user is present in name of a
                # category, then store such category
                user_categories.append(category)

    # For each matched category, store channel in that category
    # which are named 'general'
    # TODO: make channel lookup name configurable by user
    for category in user_categories:
        for channel in category_dict[category]:
            if channel.name == 'general':
                user_channels.append(channel)

    # Create webhooks for all channels in "available channel"
    for channel in user_channels:
        # Try a local lookup for webhook url
        try:
            webhook_url = CHANNEL_WEBHOOK_URL[channel.id]
        except KeyError:
            # Look whether webhook for such URL is available on Kaal backend
            status_code, webhook_url = utils.get_channel_webhook_url(channel.id)
            if not webhook_url:
                webhook = await channel.create_webhook(name='moropy_bot')
                webhook_url = webhook.url
                CHANNEL_WEBHOOK_URL[channel.id] = webhook_url
                utils.create_channel_webhook_url(channel.id, webhook_url)
        finally:
            user_webhooks.append(webhook_url)
    utils.update_users_webhook_url(userHash, user_webhooks)

    for channel in user_channels:
        await channel.send(config.MAKES_SOME_NOISE_GIF_URL)
        await channel.send(f'See who has just joined us, :eyes: <@{user.id}>')


bot.run(config.TOKEN)
