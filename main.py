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
        # get User ID
        '''
        user_id = None
        for id in db:
            if db[id] == user.name:
                print("\nye\n")
                user_id = id
        if user_id == None:
            await message.channel.send("Who are you?")
            return
        '''
        # Send answer
        text = StringPreset.str_trim(message.content, 3)
        answer = io_manager.answer(text)
        await message.channel.send(answer)


keep_alive()
client.run(os.getenv("TOKEN"))
