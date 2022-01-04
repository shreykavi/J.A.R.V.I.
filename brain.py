# brain.py

import os
import re
import discord
from dotenv import load_dotenv

from routines import open_routine, exit_routine, test_routine, sleep_routine

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# regex match for smart string processing
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
    command, app, args = ext_cmd['command'], ext_cmd['app'], ext_cmd['param']
    print(f"Received: {ext_cmd}")

    # Map to command routine
    if msg == 'test':
        await test_routine(message)
    elif command == 'open' or command == 'search':
        await open_routine(message, app, args)
    elif command == 'exit' or command == 'close':
        await exit_routine(message, app)
    elif command == 'sleep':
        await sleep_routine()
    else:
        await message.channel.send("Sorry Shrey I don't understand that command :(")

client.run(TOKEN)
