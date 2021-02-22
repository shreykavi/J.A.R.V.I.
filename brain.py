# brain.py

"""
J.A.R.V.I.S. Ideas:
- Turn on TV(periferral)
- Open app on screen (could set name to TV or main monitor etc)
    - Open game?
    - Open youtube and search (blah)
    - Open plex
    - Open netflix
- Give me a new word to learn
- Download movies, music albums, books on plexbox
- Move to Network -> Moves working dir to NAS for usage on any comp
- Computer volume (blah)

"""

import os
import random
import subprocess

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
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

    #TODO: regex match for smarter string processing!

    msg = msg.replace("JARVIS::","").lower()
    if msg == 'test':
        response = msg
        await message.channel.send(response)
    if msg == 'open netflix':
        # response = msg
        # await message.channel.send(response)
        bashCommand = "/mnt/c/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

        # TODO: extract search term from command
        # TODO: open on `preferred_screen 2` -> fix wmctrl
        search_term = "pokemon"
        args = "https://www.netflix.com/search?q=" + search_term
        process = subprocess.Popen([bashCommand, args], stdout=subprocess.PIPE)
        output, error = process.communicate()
    else:
        await message.channel.send("Sorry Shrey I don't understand that command :(")

client.run(TOKEN)