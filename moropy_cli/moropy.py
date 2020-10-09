#! ./venv/bin/python3

import click
import os
import pathlib

root_dir = ""


@click.command('register')
@click.option('-c', '--code', required=True)
def register_user(code):

    credentials_file_name = "creds"

    credentials_file_path = os.path.join(root_dir, credentials_file_name)

    if not os.path.exists(credentials_file_path):
        with open(credentials_file_path, "w") as f:
            f.write(code)
        click.echo("Successfully registered! You can continue with checking in!")
    else:
        click.echo("Already registered!")


@click.command('checkin')
def checkin():
    click.echo("I am checking in!")


@click.command('checkout')
def checkout():
    click.echo("I am checking out!")


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
