# brain.py

"""
J.A.R.V.I.S. Ideas:
- Turn on TV(periferral)
- Open app on screen (could set name to TV or main monitor etc)
    - Open game?
- Give me a new word to learn
- Download movies, music albums, books on plexbox
- Move to Network -> Moves working dir to NAS for usage on any comp
- Computer volume (blah)
- pause and play any playback
"""

import os
import random
import subprocess
from sys import platform

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# regex match for smart string processing
import re
command = re.compile(
    f"(?P<command>[a-z_]+)"
    f"( )*"
    f"(?P<app>[a-z_]*)"
    "( for )*"
    f"(?P<param>[a-z_0-9 ]*)"
)
def extract_command(message):
    regex_match = command.match(message)
    return regex_match.groupdict()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'GTFO of here {member.name}, this is Shreys private server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    print(f"> Received: {msg}")
    if msg.count("JARVIS::") != 1:
        print("Not a J.A.R.V.I.S. command.")
        return

    # Extract pieces from msg
    msg = msg.replace("JARVIS::","").lower()
    ext_cmd = extract_command(msg)
    print(f"Received: {ext_cmd}")

    if msg == 'test':
        response = msg
        await message.channel.send(response)
    elif ext_cmd['command'] == 'open' or ext_cmd['command'] == 'search':
        search_term = ext_cmd['param']
        
        if ext_cmd['app'] == 'netflix':
            args = "https://www.netflix.com/search?q=" + search_term.replace(" ", "+")
        elif ext_cmd['app'] == 'plex':
            args = "https://app.plex.tv/desktop#!/search?query=" + search_term.replace(" ", "+")
        elif ext_cmd['app'] == 'youtube':
            args = "https://www.youtube.com/results?search_query=" + search_term.replace(" ", "+")

        if platform == "darwin":
            bashCommand = "/Applications/Brave Browser.app"
            process = subprocess.Popen(['open', bashCommand, args], stdout=subprocess.PIPE)
        elif platform == "win32":
            bashCommand = "/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
            process = subprocess.Popen([bashCommand, args], stdout=subprocess.PIPE)

        # TODO: open on `preferred_screen 2` -> fix wmctrl
        
        output, error = process.communicate()
    elif ext_cmd['command'] == 'teamviewer':
        if platform == "darwin":
            await message.channel.send("JARVIS-OSX doesn't do teamviewer :S") 
            return
        bashCommand = "/mnt/c/Program Files (x86)/TeamViewer/TeamViewer.exe"
        process = subprocess.Popen([bashCommand], stdout=subprocess.PIPE)
    else:
        await message.channel.send("Sorry Shrey I don't understand that command :(")

client.run(TOKEN)
