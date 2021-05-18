import click
import os
from  cli.cliCommands import starApp

os.environ['LC_ALL'] = 'en_US.utf-8'
os.environ['LANG'] = 'en_US.utf-8'

print("Hello, Welcome to Cowin Vaccine finder tool!")


@click.group()
@click.pass_context
def main(ctx):
    if ctx.obj is None:
        ctx.obj = {}

main.add_command(starApp)