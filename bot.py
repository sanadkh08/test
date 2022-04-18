from http import client
from urllib import response
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "misrable", "depressing"]

starter_enc = [
    "nigga",
    "black balls !",
    "gigantic balls",
    "bitch niggery bitch black balls",
] 



def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def update_cor(enc_message):
    if "enc" in db.keys():
        enc = db["enc"]
        enc.append(enc_message)
        db["enc"] = enc
    else:
        db["enc"] = [enc_message]

def del_enc(index):
    enc = db["enc"]
    if len(enc) > index:
        del enc[index]
        db["enc"] = enc

@client.event
async def on_ready():
    print("WE have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

    msg = message.content

    if message.author == client.user:
        return

    if msg.startswith("$عمو"):
        quote = get_quote()
        await message.channel.send(quote)
    
    options = starter_enc
    if "enc" in db.keys():
        options = options + db["enc"]

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        enc_msg = msg.split("$new ", 1)[1]
        update_cor(enc_msg)
        await message.channel.send("New enc msg added.")

    if msg.startswith("$del"):
        enc = []
        if "enc" in db.keys():
            index = msg.split("$del", 1)[1]
            del_enc(index)
            enc = db["enc"]
        await msg.channel.send(enc)


keep_alive()
client.run("OTY1MzE4NzgxNDk0NzY3Njk3.YlxdLA.5kRGZavTUyhTap-MrE2ev-lFeQ4")