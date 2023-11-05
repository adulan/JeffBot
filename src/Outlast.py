import discord
from datetime import datetime
from src.constants import DISCORD_TOKEN

# Define the Discord client with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


# Define an event handler for when the client connects to Discord
@client.event
async def on_ready():
    print("Logged in as {0.user}.".format(client))
    print(datetime.now())
    _setup()
    await populate_survivors(client)


# Define an event handler for when a message is sent in a channel
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    
    # check if the message is a command
    if message.content.startswith("!"):
        await process_command(message, client)

def _setup():
    # Create all needed files
    with open("players.csv", 'w+'):
        pass

    with open("tribes.csv", 'w+') as f:
        f.write("voting,none\n")

    with open("vote_time", 'w+') as f:
        f.write('0')

    with open("idols.csv", 'w+') as f:
        pass

    with open("token", 'w+') as f:
        f.write(input("Token: "))

    with open("playernum", 'w+') as f:
        f.write("0")

# Run the client with the Discord API token
client.run(DISCORD_TOKEN)