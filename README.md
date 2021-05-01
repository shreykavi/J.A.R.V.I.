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

# Description
This works with commands that prefix with `JARVIS::` and then the actual command.
Ex. `JARVIS::test`

List of current commands:
test - Reply with 'test'
(open|search) (netflix|plex|youtube) for {any text here} - open Brave with app on a search term