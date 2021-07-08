import discord
import os
import time
from stay_awake import keep_alive
import io_manager
import TextManagement.StringPreset as StrP

client = discord.Client()

IDs = ["Blind Fish", "Trainerd", "Dilara", "elli", "Ian", "jamila", "jila", "lara", "Lisa", "Logikerus", "Emilia"]

# Run Bot
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    user = message.author
    if user == client.user:
        return

    if message.content.startswith("!i "):
        # get content
        msg_split = message.content.split("||")

        # get user id
        user_id = StrP.str_trim(msg_split[0], 3)

        # get text
        text = StrP.str_trim(str(msg_split[1]), 1)

        # translate and send
        translation_1 = io_manager.transition(text, user_id, 25)
        translation_2 = io_manager.transition(text, user_id, 75)
        response_1 = IDs[int(user_id)] + " 25%:\n" + translation_1
        response_2 = IDs[int(user_id)] + " 75%:\n" + translation_2
        await message.channel.send(response_1)
        time.sleep(10)
        await message.channel.send(response_2)
    
    elif message.content.startswith("!u "):
        # get content
        msg_split = message.content.split("||")

        # get intensity
        intensity = StrP.str_trim(msg_split[0], 3)

        # get text
        text = StrP.str_trim(str(msg_split[1]), 1)

        # translate and send
        for user_id in range(11):
          translation = io_manager.transition(text, user_id, intensity)
          response = IDs[int(user_id)] + " " + str(intensity) + "%:\n" + translation
          await message.channel.send(response)
          time.sleep(5)



keep_alive()
client.run(os.getenv("TOKEN"))
