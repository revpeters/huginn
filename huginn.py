import click
import requests
import json
import time
import paramiko
import random
import os
import sys
from rich import print
from rich.console import Console
from pytz import timezone

api_weather = "88646510c8b72cc12b572451639dcc95"

console = Console()


@click.group()
def cli():
    """One of Odin's ravens"""
    pass


@cli.command()
@click.option('--location', default='Raleigh,US-NC')
def weather(location):
    """get me weather information"""

    url_params = "&units=imperial"
    url_weather = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_weather}{url_params}"
    response = requests.get(url_weather)
    json_weather = response.json()
    info_weather = json_weather["weather"][0]
    temps_weather = json_weather["main"]
    sunrise_weather = time.strftime(
        "%l:%M:%S %p", time.localtime(json_weather["sys"]["sunrise"]))
    sunset_weather = time.strftime(
        "%l:%M:%S %p", time.localtime(json_weather["sys"]["sunset"]))
    click.echo(f'Getting weather for {location}\n')
    click.echo(
        f'The weather in {location} : {info_weather["description"]} @ {temps_weather["feels_like"]} degrees.\n')
    click.echo(f'Sunrise @ {sunrise_weather}')
    click.echo(f'Sunset  @ {sunset_weather}')


@cli.command()
def traffic():
    """get me traffic information from around my location"""
    click.echo('calling traffic command')


@cli.command()
def remind():
    """Is there anything important going on today
    or something I need to start working on"""
    click.echo('calling remind command')


@cli.command()
def note():
    """Save information you want to keep or need to be reminded about at a future date"""
    click.echo(click.style('calling note command', fg="yellow"))
    taken_note = 'I am taking a note'
    click.echo(click.style(taken_note, fg="green"))


@cli.command()
@click.option('-c', '--command', default='uptime')
def cluster(command):
    """Check state of Turing Pi cluster"""
    nodes = ['cm-node-01', 'cm-node-02', 'cm-node-03',
             'cm-node-04', 'cm-node-05', 'cm-node-06', 'cm-node-07']
    for node in nodes:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(node, 22, 'pirate')
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        click.echo(f'\n{node}\n')
        for line in lines:
            line = line.rstrip('\n')
            click.echo(f'\t\b\b{line}')


@cli.command()
def rhcsa():
    """Give me a random command or system file that will be used during the RHCSA exam
    with important flags to remember"""

    '''
    commands:
        groupadd
        useradd
        chage

    files:
        /etc/login.defs
        /etc/sudoers(.d/)
    '''
    def show_notes(note):
        with open(os.path.join(os.path.dirname(__file__), f'commands_files/{note}_notes'), 'r') as f:
            lines = f.read().splitlines()
            #click.secho(f.read(), fg="green")

        for line in lines:
            console.print(line, highlight=False)

    commands_files = ['groupadd', 'useradd', 'chage', 'login.defs', 'sudoers']
    note = commands_files[random.randint(0, len(commands_files)-1)]
    show_notes('chage')


@cli.command()
def colors():
    """Print an examle and hex codes of Aurora color swatch"""
    """ colors_list = {
        'chestnut': '#BF616A',
        'light_red': '#e38891',
        'Antique Brass': '#D08770',
        'yellow': '#EBCB8B',
        'green': '#A3BE8C',
        'purple': '#B48EAD',
        'light_purple': '#dbc5d7',
        'blue': '#5E81AC',
        'light_blue': '#85ADDE',
        'yellow green': '#B8E067',
        'jungle green': '#2FAB63',
        'pine green': '#007076',
        'blue other': '#006AB3'
    } """

    colors_list = {
        'can can': '#DA9BB7',
        'chestnut': '#BF616A',
        'Antique Brass': '#D08770',
        'putty': '#EBCB8B',
        'Kournikova': '#FFE979',
        'pastel green': '#84E882',
        'Ocean Green Pearl': '#4BBC8E',

        'steel blue': '#4A8EB4',
        'cornflower': '#85ADDE',
        'violet purple': '#936DAA',
        'Strikemaster': '#825882',

    }

    swatch_two = {
        'festival': '#F9F871',
        'yellow green': '#B8E067',
        'mantis': '#78C664',
        'jungle green': '#2FAB63',
        'deep sea': '#008E63',
        'strong cyan': '#007160'
    }

    swatch_three = {
        'Pickled Bluewood': '#2F4858',
        'Blue Bayoux': '#485A73',
        'Storm Gray': '#676A8B',
        'Trendy Pink': '#8C7A9F',
        'Bouquet': '#B38AAE',
        'Rose Dust': '#A55A7B',
        'can can': '#DA9BB7'
    }

    swatch_four = {
        'chestnut': '#BF616A',
        'Rose Dust': '#A55A7B',
        'Strikemaster': '#825882',
        'Smoky': '#5E567D',
        'fiord': '#40506D'
    }

    for color in colors_list:
        console.print(f'[{colors_list[color]}]{color.upper()}'.ljust(
            30) + f' {colors_list[color]}[/{colors_list[color]}]')

    """for color in swatch_two:
        console.print(f'[{swatch_two[color]}]{color.upper()}'.ljust(
            30) + f' {swatch_two[color]}[/{swatch_two[color]}]')

    for color in swatch_four:
        console.print(f'[{swatch_four[color]}]{color.upper()}'.ljust(
            30) + f' {swatch_four[color]}[/{swatch_four[color]}]')

    for color in swatch_three:
        console.print(f'[{swatch_three[color]}]{color.upper()}'.ljust(
            30) + f' {swatch_three[color]}[/{swatch_three[color]}]')"""
