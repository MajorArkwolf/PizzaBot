import discord
import os
from dotenv import load_dotenv
from os.path import join, dirname

client = discord.Client()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# The trust channels to look for free pizza
trusted_channel = [718113875203063899, 605754665732407316]
# The trusted people who will bestow the free pizza
trusted_people = [184291535221817348, 465038624170180609, 210742437553897473, 223816914974015488, 315047494151176192, 275281624386633728]
# The bois to tell to claim said free pizza
the_true_boy = 184291535221817348
# The key words to look for when pizza is available
key_words = ["pizza", "free", "BBQ", "chicken", "some like it hot", "hot", "supreme", "meat", "lovers", "lover", "Got a", "pepperoni", "family size", "hawaiian", "hawian"]


async def notify_the_boi(message):
    user = await client.fetch_user(the_true_boy)
    send_message = discord.Embed(title="Pizza Alert")
    send_message.add_field(name=f"User: {message.author}", value=f"{message.content}", inline=True)
    new_message = await user.send(embed=send_message)
    await new_message.add_reaction("✅")


async def confirm_the_pizza(message):
    pass


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(message.channel.id == x for x in trusted_channel):
        if any(message.author.id == x for x in trusted_people):
            if any(x.lower() in message.content.lower() for x in key_words):
                await notify_the_boi(message)


@

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
