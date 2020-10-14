from logging import Logger

import requests
from config import KAAL_BACKEND_URL

logger = Logger(__name__)

REGISTER_USER_ENDPOINT = '/register/'
CHANNEL_WEBHOOK_ENDPOINT = '/channel/{}'
USER_WEBHOOKS_ENDPOINT = '/storechannel'
USER_VALIDATE_ENDPOINT = '/validatebot/'
POD_DETAILS_ENDPOINT = '/summary/'


def _get_absolute_url(relative_url):
    return KAAL_BACKEND_URL + relative_url


def registerUser(discord_user_id, discord_username, discord_roles):
    response = requests.post(
        url=_get_absolute_url(REGISTER_USER_ENDPOINT),
        json={
            "userId": discord_user_id,
            "userName": discord_username,
            "roles": discord_roles,
        },
    )
    return (response.status_code, response.json().get('userHash', None))


def get_channel_webhook_url(channel_id):
    response = requests.get(
        url=_get_absolute_url(CHANNEL_WEBHOOK_ENDPOINT.format(channel_id)),
    )
    return response.status_code, response.json().get('userHash', None)


def create_channel_webhook_url(channel_id, webhook_url):
    response = requests.post(
        url=_get_absolute_url(CHANNEL_WEBHOOK_ENDPOINT.format(channel_id)),
        json={'webhook_url': webhook_url},
    )
    return response.status_code, response.json().get('webhook_url', None)


def update_users_webhook_url(userHash, webhook_urls):
    response = requests.post(
        url=_get_absolute_url(USER_WEBHOOKS_ENDPOINT),
        json={'userHash': userHash, 'webhookUrls': webhook_urls},
    )
    status_code = response.status_code
    if response.status_code != 200:
        logger.warn(f'Users webhook URLs update failed, status code: {status_code}')
    return status_code, None


def validate_user(user_id):
    response = requests.post(
        url=_get_absolute_url(USER_VALIDATE_ENDPOINT), json={"userID": str(user_id)}
    )
    if response.status_code == 404:
        return False, None
    return response.json().get('status', False), response.json().get('userHash', None)


def get_pod_availability_status(role):
    response = requests.post(
        url=_get_absolute_url(POD_DETAILS_ENDPOINT), json={"role": str(role)}
    )
    return response.status_code, response.json().get('msg', None)


def get_pod_leaderboard(role):
    response = requests.post(
        url=_get_absolute_url(POD_DETAILS_ENDPOINT), json={"role": str(role)}
    )
    return response.status_code, response.json().get('msg', None)
