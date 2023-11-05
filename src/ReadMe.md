# https://github.com/kraklo/JeffBot/blob/master/ext.py

# Jeff Bot

Jeff Bot is made for Discord and simulates a game of Survivor.

## Discord Permissions

To function fully, Pope Bot requires the `SERVER MEMBERS INTENT` and `MESSAGE CONTENT INTENT` Priviliged Gateway Intents

It also requires the following Bot Permissions

`Send Mesages`

`Manage Mesages`

`Use External Emojis`

`Add Reactions`

`Read Messages/View Channels`

`Mention @everyone, @here, and All Roles`

`Attach Files`

## Run Locally

`docker build --pull --rm -f "Dockerfile" -t popebot:latest "."`

```
docker run -it \
--env DISCORD_TOKEN="YOUR_TOKEN" \
--env GUILD_ID="YOUR_SERVER_ID" \
--env POPELINESS_CHANNEL_ID="YOUR_CHANNEL_ID" \