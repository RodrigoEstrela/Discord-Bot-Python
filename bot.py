# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


# ON_READY
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


# ON_MEMBER_JOIN
@bot.event
async def on_member_join(member):
    guild = discord.utils.get(bot.guilds, name=GUILD)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello there, {member.name}, welcome to {guild.name}!'
    )


# RANDOM NUMBER GENERATOR
@bot.command(name='random_num', help='Returns a random number from 0 to 4242')
async def rannum(ctx):
    await ctx.send(random.randint(0, 4243))


# TRUTHS ABOUT 42
@bot.command(name='42', help='Shows an objective truth about 42')
async def quarentaedois(ctx):
    objective_truths = [
        '42 is amazing!',
        '42 is the best school!',
        '42 mega elite!',
        '42 network > every other school',
        '42 gigachad school',
        '42 Amsterdam > cOdAM',
        '42 Helsinki > hIvE'
    ]

    selected_truth = random.choice(objective_truths)
    await ctx.send(selected_truth)


# MEANING OF LIFE
@bot.command(name='sentido_da_vida', help='Enlightens the user!')
async def life_meaning(ctx):
    await ctx.send('42, a tua mãe de 4 e eu de 2.\n   -Antonio Vieira, 2022')


# CREATE CHANNEL
@bot.command(name='create-channel', help='Creates a new channel')
@commands.has_role('TECHNOROYALCOUNSIL')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


# ON_ERROR
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)
