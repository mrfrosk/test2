import discord
hey = ["привет", "здарова","ку"]
from discord.ext import commands
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
client = discord.Client()

@client.event
async def on_message(message):
    b = message.content.split(" ")
    if b[0] in hey:
        await message.channel.send(f"ну {b[0]}")



client.run("NzY2MjIwOTI0MjQzNTQyMDI2.X4gM2A.eAttSnUvLsWwFvlJRDMau3ymajA")