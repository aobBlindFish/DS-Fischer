import discord
import os
import time
from stay_awake import keep_alive
import io_manager
import TextManagement.StringPreset as StrP

client = discord.Client()

IDs = [
    "Blind Fish", "Trainerd", "Dilara", "Elli", "Ian", "Jamila", "Jila",
    "Lara", "Lisa", "Logikerus", "Emilia"
]


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
        translation_1 = io_manager.transition(text, user_id, 10)
        translation_2 = io_manager.transition(text, user_id, 50)
        translation_3 = io_manager.transition(text, user_id, 90)
        response_1 = IDs[int(user_id)] + " 10%:\n" + translation_1
        response_2 = IDs[int(user_id)] + " 50%:\n" + translation_2
        response_3 = IDs[int(user_id)] + " 90%:\n" + translation_3
        await message.channel.send(response_1)
        time.sleep(5)
        await message.channel.send(response_2)
        time.sleep(5)
        await message.channel.send(response_3)

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
            response = IDs[int(user_id)] + " " + str(
                intensity) + "%:\n" + translation
            await message.channel.send(response)
            time.sleep(5)

    elif message.content.startswith("!s "):
        # get content
        msg_split = message.content.split("||")

        # get user id
        user_id = StrP.str_trim(msg_split[0].split(";")[0], 3)

        # get intensity
        intensity = StrP.str_trim(msg_split[0].split(";")[1], 1)

        # get text
        text = StrP.str_trim(str(msg_split[1]), 1)

        # translate and send
        translation = io_manager.transition(text, user_id, intensity)
        response = IDs[int(user_id)] + " " + str(
            intensity) + "%:\n" + translation
        await message.channel.send(response)

    elif message.content.startswith("!c "):
        # get intensity
        intensity = StrP.str_trim(message.content, 3)

        # Generate Conversation
        msgs = io_manager.conversation(intensity)
        title = msgs[0]
        lines = msgs[2]
        names = ""
        for id in msgs[1]:
            names = names + IDs[id] + ", "

        names = StrP.str_trim(names, -2)

        # Send Intro
        introduction = "Gespräch: " + title + "\nPersonen: " + names
        await message.channel.send(introduction)

        # Send Conversation
        for line in lines:
            time.sleep(5)
            await message.channel.send(line)
        
        # Stop Conversation
        time.sleep(3)
        await message.channel.send("Ende")


keep_alive()
client.run(os.getenv("TOKEN"))
