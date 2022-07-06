# bot.py
import os
import random

#import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


#intents = discord.Intents.default()
#intents.members = True
#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!')

'''
@client.event  # on_ready
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event  # on_member_join
async def on_member_join(member):
    guild = discord.utils.get(client.guilds, name=GUILD)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello there, {member.name}, welcome to {guild.name}!'
    )


@client.event  # on_message
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!random_nu':
        await message.channel.send(random.randint(0, 4243))
    elif message.content == 'raise-exception':
        raise discord.DiscordException
'''


@bot.command(name='42', help='Shows an objective truth about 42')
async def quarentaedois(ctx):
    objective_truths = [
        '42 is amazing!',
        '42 is the best school!',
        '42 mega elite!',
        '42 network > every other school',
        '42 gigachad school'
    ]

    selected_truth = random.choice(objective_truths)
    await ctx.send(selected_truth)


@bot.command(name='sentido_da_vida', help='Enlightens the user!')
async def life_meaning(ctx):
    await ctx.send('42, a tua mãe de 4 e eu de 2.\n   -Antonio Vieira, 2022')


'''@client.event  # on_error
async def on_error(event, *args):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'\nUnhandled message: {args[0]}1n\n\n')
        else:
            raise
'''
bot.run(TOKEN)

