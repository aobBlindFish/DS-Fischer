import discord
import os
from stay_awake import keep_alive
import io_manager
import StringPreset
from replit import db

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

    if message.content.startswith("!f "):
        # get Username
        username = user.name + "#" + user.discriminator

        # get User ID
        user_id = None
        for id in db:
            if db[str(id)] == username:
                user_id = id
        if user_id == None:
            await message.channel.send("Who are you?")
            return

        # Send answer
        text = StringPreset.str_trim(message.content, 3)
        answer = io_manager.answer(text, user_id)
        await message.channel.send(answer)

    if message.content.startswith("!n "):
        print("1. ")
        await client.user.edit(username="Birne")
        print("2. ")


keep_alive()
client.run(os.getenv("TOKEN"))
