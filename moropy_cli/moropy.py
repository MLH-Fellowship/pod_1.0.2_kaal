#! ./venv/bin/python3

import click


@click.command('register')
def register_user():
    click.echo("I am registering")


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
    pass


init_cli.add_command(register_user)
init_cli.add_command(checkin)
init_cli.add_command(checkout)
init_cli.add_command(set_away)
init_cli.add_command(set_available)


if __name__ == '__main__':
    init_cli()
