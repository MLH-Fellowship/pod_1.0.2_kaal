#! ./venv/bin/python3

import os
import pathlib
import subprocess

import click

root_dir = ""
credentials_file_name = "creds"
status_file_name = "status"


@click.command('register')
@click.option('-c', '--code', required=True)
def register_user(code):
    credentials_file_path = os.path.join(root_dir, credentials_file_name)

    with open(credentials_file_path, "w") as file:
        file.write(code)
    click.echo("Successfully registered! You can continue with checking in!")


@click.command('checkin')
def checkin():
    credentials_file_path = os.path.join(root_dir, credentials_file_name)

    with open(credentials_file_path, "rb") as file:
        user_hash = file.readline().decode('UTF-8')
        print("Checking in for", user_hash)

    subprocess.call("chmod +x ./ticker.py", shell=True)
    subprocess.call("nohup ./ticker.py", shell=True)


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
    click.echo("I am away!")


@click.command('available')
def set_available():
    click.echo("I am available!")


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