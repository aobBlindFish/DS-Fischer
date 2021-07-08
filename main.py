import discord
import os
from stay_awake import keep_alive
import io_manager
import TextManagement.StringPreset as StrP

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
        # get content
        msg_split = message.content.split("|||")

        # get user id
        user_id = StrP.str_trim(msg_split[0].split(", ")[0], 3)

        # get intensity
        intensity = msg_split[0].split(", ")[1]

        # get text
        text = StrP.str_trim(str(msg_split[1]), 1)

        # translate and send
        translation = io_manager.transition(text, user_id, intensity)
        await message.channel.send(translation)


keep_alive()
client.run(os.getenv("TOKEN"))
