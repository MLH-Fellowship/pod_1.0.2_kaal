import requests

HOST_URL = 'https://kaal-backend.herokuapp.com'

REGISTER_USER_ENDPOINT = '/register/'


def get_absolute_url(relative_url):
    return HOST_URL + relative_url


def registerUser(discord_user_id, discord_username, discord_roles):
    response = requests.post(
        url=get_absolute_url(REGISTER_USER_ENDPOINT),
        json={
            "userId": discord_user_id,
            "userName": discord_username,
            "roles": discord_roles,
        },
    )
    return (response.status_code, response.json().get('userHash', None))
