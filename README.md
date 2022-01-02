# J.A.R.V.I.S.
This is a home automation discord bot which automatically does things for me when I'm too lazy to go to my desk. 

To run:
1. Setup a discord bot
2. Get your bots Token and Guid and add to a `.env` file as follows:
```
DISCORD_TOKEN=xxx
DISCORD_GUILD=xxx
```

# Run at startup on OSX
add the osx-start.sh file to "System Preference -> Users and Groups -> Login items"

# Run at startup on Windows 7+
1. Open 'run' and run the command `shell:startup`
2. Create shortcut to run.bat and move shortcut to the Startup folder that was just opened
3. Right click on shortcut, click on properties and set Run to minimized so it doesn't pop up on startup

# Description
This works with commands that prefix with `JARVIS::` and then the actual command.
Ex. `JARVIS::test`

List of current commands:
test - Reply with 'test'
(open|search) (netflix|plex|youtube) for {any text here} - open Brave with app on a search term