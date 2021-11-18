import discord
from discord.ext import tasks
import datetime
import random
import math
from replit import db
import os
from stay_awake import keep_alive
import io_manager as io

client = discord.Client()

IDs = ["Blind Fish#9878", "Dilara#1623"]
cmd_error = [
    "Hast du einen Befehl benutzt? Diesen Befehl habe ich nicht verstanden.",
    "Der Befehl, den du benutzen wolltest, war für mich zu unverständlich."
]
tt_received = ["Ich habe den Link aufgenommen.", "Der Link wurde gespeichert."]
alerts = ["Neues TikTok für dich!\n", "Gönn dir!\n"]


# Run Bot
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))
    send_tt.start()


#send link
frequency = round(
    random.uniform((24 * 60 * 60 / (math.e**0.5)),
                   (24 * 60 * 60 / (math.e**(1 / math.e)))))


@tasks.loop(seconds=frequency)
async def send_tt():
    for u_name in IDs:
        get_id = u_name.split("#")[0]
        user_app_id = os.getenv(get_id)
        user_rec = await client.fetch_user(user_app_id)

        link_list = []
        #collect all links going to u_name
        for key in db.keys():
            if db[key].split(";;;")[0] == u_name:
                link_list.append([key, db[key].split(";;;")[1]])
        #send a random link
        if len(link_list) != 0:
            link = random.choice(link_list)
            await user_rec.send(random.choice(alerts) + link[1])
            del db[link[0]]
            #document
            print("msg sent to", u_name + ":",
                  datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


@client.event
async def on_message(message):
    user = message.author
    if user == client.user:
        return

    if message.content.startswith("!"):  #command
        await message.channel.trigger_typing()
        if message.content.startswith("!tiktok\n"):  #tiktok
            link_list = message.content.splitlines()[1:]
            if str(user) == IDs[1]:
                receiver = IDs[0]
            else:
                receiver = IDs[1]
            #add to db
            for link in link_list:
                if len(link) != 0:
                    entry = receiver + ";;;" + link
                    db[str(random.randint(0, 10**10))] = entry
            try:
                uid = IDs.index(str(user))
                await message.channel.send(
                    io.transition(random.choice(tt_received), uid, 50))
            except ValueError:
                await message.channel.send(random.choice(tt_received))
        elif message.content.startswith("!t;"):  #dm transform
            pass
        elif message.content.startswith("!n;"):  #dm normal
            pass
        elif message.content.startswith("!a;"):  #dm adressed
            pass
        else:  #command error message
            try:
                uid = IDs.index(str(user))
                await message.channel.send(
                    io.transition(random.choice(cmd_error), uid, 50))
            except ValueError:
                await message.channel.send(random.choice(cmd_error))


keep_alive()
client.run(os.getenv("TOKEN"))
