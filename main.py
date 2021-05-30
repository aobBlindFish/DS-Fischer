import discord
import os
from stay_awake import keep_alive
import StringPreset
import data

client = discord.Client()


# Databsae
def add_value(value):
    print("ye")


# Run Bot
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    user = message.author
    if user == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("hi")

    elif message.content.startswith("!add"):
        if (StringPreset.str_trim(message.content, 4) + " ").isspace():
            await message.channel.send("add what?")
        else:
            msg_value = StringPreset.str_trim(message.content, 5).split(" ")[0]
            msg_key = StringPreset.str_trim(message.content, 5).split(" ")[1]
            if data.add_entry(msg_value, msg_key):
                await message.channel.send('Word "' + msg_value + '" added.')
            else:
                await message.channel.send("couldnt add.")

    elif message.content.startswith("!del"):
        if (StringPreset.str_trim(message.content, 4) + " ").isspace():
            await message.channel.send("delete what?")
        else:
            key = StringPreset.str_trim(message.content, 5)
            await message.channel.send(data.delete_entry(key))

    elif message.content.startswith("!read"):
        if not StringPreset.str_trim(message.content, 5):
            read_key = " "
        else:
            read_key = StringPreset.str_trim(message.content, 6)
        await message.channel.send(data.read_db(read_key))

    elif message.content.startswith("!change"):
        if (StringPreset.str_trim(message.content, 7) + " ").isspace():
            await message.channel.send("change what?")
        else:
            old_value = StringPreset.str_trim(message.content, 8).split(" ")[0]
            old_key = StringPreset.str_trim(message.content, 8).split(" ")[1]
            new_value = StringPreset.str_trim(message.content, 8).split(" ")[2]
            await message.channel.send(
                data.update_entry(old_value, old_key, new_value))

keep_alive()
client.run(os.getenv("TOKEN"))
