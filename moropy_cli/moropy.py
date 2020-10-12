#! ./venv/bin/python3

import json
import os
import pathlib
import subprocess

import click
import requests

root_dir = ""
credentials_file_name = "creds"
status_file_name = "status"
base_url = "https://kaal-backend.herokuapp.com"


@click.command('register')
@click.option('-c', '--code', required=True)
def register_user(code):
    credentials_file_path = os.path.join(root_dir, credentials_file_name)

    # section to contact the backend API to validate code

    response = requests.post(
        "{}/validate".format(base_url), json.dumps({"userHash": code})
    )

    if response.status_code == 401:
        print("Invalid Token. Please try again!")
        return

    if response.status_code != 200:
        print("Server error. please contact admin.")
        return

    response_data = response.json()

    print(response_data)

    username = "zerefwayne"

    with open(credentials_file_path, "w") as file:
        file.write(code)
        file.write('\n')
        file.write(username)

    click.echo(
        "Successfully registered {}! You can continue with checking in!".format(
            username
        )
    )


@click.command('checkin')
def checkin():
    credentials_file_path = os.path.join(root_dir, credentials_file_name)

    with open(credentials_file_path, "rb") as file:
        user_hash = file.readline().decode('UTF-8')
        user_name = file.readline().decode('UTF-8')

        print("Checking in for", user_name, user_hash)

    subprocess.call("chmod +x ./ticker.py", shell=True)
    subprocess.call("nohup ./ticker.py >/dev/null 2>&1 &", shell=True)


@click.command('checkout')
def checkout():
    status_file_path = os.path.join(root_dir, status_file_name)

    if not os.path.exists(status_file_path):
        print(status_file_path, "doesn't exist")
        return

    # writes close status to moropy.sh
    with open(status_file_path, 'w') as file:
        file.write("0")


@click.command('away')
def set_away():

    click.echo("Setting away")

    credentials_file_path = os.path.join(root_dir, credentials_file_name)

    with open(credentials_file_path, "rb") as file:
        user_hash = file.readline().decode('UTF-8')[:-1]
        user_name = file.readline().decode('UTF-8')

        data = {'userHash': user_hash, 'status': 'away'}

        res = requests.post("{}/status/".format(base_url), json.dumps(data))

        print(res.json())


@click.command('available')
def set_available():

    click.echo("Setting available")

    credentials_file_path = os.path.join(root_dir, credentials_file_name)

    with open(credentials_file_path, "rb") as file:
        user_hash = file.readline().decode('UTF-8')[:-1]
        user_name = file.readline().decode('UTF-8')

        data = {'userHash': user_hash, 'status': 'available'}

        res = requests.post("{}/status/".format(base_url), json.dumps(data))

        print(res.json())


@click.group()
def init_cli():

    print("Initalizing Moropy")
    user_home_dir = pathlib.Path.home()

    global root_dir
    root_dir = pathlib.Path.joinpath(user_home_dir, ".moropy")

    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
        click.echo("generated {}".format(root_dir))


init_cli.add_command(register_user)
init_cli.add_command(checkin)
init_cli.add_command(checkout)
init_cli.add_command(set_away)
init_cli.add_command(set_available)

if __name__ == '__main__':
    init_cli()
