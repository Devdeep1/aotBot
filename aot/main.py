# Main Imports
import discord
import random
import interactions

# Sub Imports
from discord.ui import Button, View

# Imports from files
import variables as v
import colors as c

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.members = True

client = discord.Client(intents=intents)
command_prefix = "."


@client.event
async def on_ready():
    print("online...")


@client.event
async def on_message(message):


    if message.content == "nice":
        await message.channel.send("very nice")

    if message.content == command_prefix + "ping":
        global ping_count

        embed = discord.Embed(
            title="pong",
            description=f"number of pings this session {v.ping_count}",
            color=c.blue
        )
        await message.channel.send(embed=embed)

        v.ping_count = v.ping_count + 1

    if message.content == command_prefix + "go":

        embed = discord.Embed(
            title="documentation",
            description="click the tile for documentation for the bot",
            url="https://www.youtube.com/watch?v=gaceByQIVmU",
            color=c.blue
        )
        await message.channel.send(embed=embed)

    if message.content == command_prefix + "combat":

        combat_length = random.randrange(5, 10)
        

        # embeds
        combat_length_embed = discord.Embed(color=discord.Color.red(), title=f'you have {combat_length} moves')
        choices_embed = discord.Embed(color=discord.Color.red(), title='make your move', description='click on the respective button to make your move')

        # buttons
        button1 = Button(label="button 1", style=discord.ButtonStyle.green)
        button2 = Button(label="button 2", style=discord.ButtonStyle.green)
        buttonView = [button1, button2]

        await message.channel.send(embed=combat_length_embed, Button=button1)
        view = View()
        view.add_item(buttonView)

        moves = ["R", "L"]
        choices = []

        await message.channel.send(embed=choices_embed)
        await message.channe.send("make your choice", view=view)

        for i in range(0, combat_length):
            rand = random.choice(moves)
            v.a.append(rand)


            


token = ''
client.run(token)


