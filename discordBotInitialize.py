# id : 698851404588253254
# token : Njk4ODUxNDA0NTg4MjUzMjU0.XpL8UQ._5QlLDLpcwR0pgaKxsg5WTeY6q8
# permission int : 67648
# https://discordapp.com/api/oauth2/authorize?client_id=698851404588253254&scope=bot&permissions=67648

import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "INDICATOR" in message.content.lower():
        await message.channel.send("ANSWER")

client.run("Njk4ODUxNDA0NTg4MjUzMjU0.XpL8UQ._5QlLDLpcwR0pgaKxsg5WTeY6q8")