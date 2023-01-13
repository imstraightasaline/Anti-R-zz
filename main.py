import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

import pymongo
from datetime import timedelta

client = pymongo.MongoClient("mongodb+srv://authAdmin:5k3E6mEdjDX8rSwT@tomscluster.wwos8ih.mongodb.net/?retryWrites=true&w=majority")
mainDb = client.antirizz

client = commands.Bot(command_prefix = "ar!", intents = intents, activity = discord.Streaming(name = "No r*zz!!!!!", url = "https://youtu.be/AUJAysi0yHM"))

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    try:
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} commands.')
    except Exception as e:
        print(e)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "rizz" in message.content.lower():
        await message.channel.send("No r*zz!!!!!")
        doc = mainDb.antirizz.find_one({ "userID": message.author.id })

        if doc is None:
            key = {
            "userID": message.author.id,
            "count": 1
            }
            mainDb.antirizz.insert_one(key)
        else:
            doc = mainDb.antirizz.find_one({ "userID": message.author.id })
            count = doc["count"]
            newcount = count + 1
            mainDb.antirizz.update_one({ "userID": message.author.id }, { "$set": { "count": newcount }})
        doc = mainDb.antirizz.find_one({ "userID": message.author.id })
        newcount = doc["count"]
        delta = timedelta(minutes = 5)
        await message.author.timeout(delta, reason = "No r*zz!!!!!")
        await message.channel.send(f"Hah, get timed out nerd! ||{newcount}||")
        return

client.run("############################")
