import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
SERVER_ID = os.getenv('DISCORD_SERVER_ID')

LOADING_GIF_URL = (
    'https://tenor.com/view/rofl-okaay-please-stand-by-in-progress-loading-gif-13829297'
)
BOOM_GIF_URL = 'https://tenor.com/view/explosion-boom-iron-man-gif-14282225'
MAKES_SOME_NOISE_GIF_URL = 'https://tenor.com/view/kshmr-make-some-noise-gif-11076929'
DOCUMENTATION_URL = 'https://github.com/MLH-Fellowship/pod_1.0.2_kaal#kaal'
KAAL_BACKEND_URL = os.getenv('KAAL_BACKEND_URL')
