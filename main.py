# Deutschland
import discord
import os
import time
from stay_awake import keep_alive


client = discord.Client()


# Run Bot
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    user = message.author
    if user == client.user:
        return


keep_alive()
client.run(os.getenv("TOKEN"))
