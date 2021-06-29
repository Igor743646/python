import discord
import os
from GetPicture import GetPicture

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$I am sad('):
        await message.channel.send("Don't worry! You're beautifull as usually!! I love you:3")

    if message.content.startswith('$get me picture'):
    	await message.channel.send(GetPicture(" ".join(message.content.split(' ')[3:])))

client.run('ODUzMjU1ODgwODkxMzAxODkw'+'.'+'YMSudg'+'.'+'b3xgg_WdqqirTgORXJRb_iDPvwE')