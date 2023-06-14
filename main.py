import sys
sys.path.insert(0, 'discord.py-self')
sys.path.insert(0, 'discord.py-self_embed')

import discord
from discord.ext import commands
import discord_self_embed
import json

with open('config.json', 'r') as file:
    config = json.load(file)
  
token = config['token']
prefix = config['prefix']

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.command()
async def embed(ctx):
    embed = discord_self_embed.Embed("Test Title", 
      description="Very cool Description!", 
    )
    embed.set_author(f"{ctx.author}")

    url = embed.generate_url(hide_url=True)
    await ctx.send(url)

@bot.command()
async def create_role(ctx, role):
    role = await ctx.guild.create_role(name=role)
    print(f"Role Created: {role.name} ({role.id})")
  
@bot.command()
async def create_channel(ctx, channel):
    channel = await ctx.guild.create_text_channel(name=channel)
    print(f"Channel Created: {channel.name} ({channel.id})")
  

@bot.command()
async def msg(ctx, user: discord.Member, *, message):
    await user.send(message)
    print(f"Message Sent: {message} to {user.name} ({user.id})")

@bot.command()
async def kick(ctx, user: discord.Member):
    await user.kick()
    print(f"Kicked: {user.name} ({user.id})")

@bot.command()
async def ban(ctx, user: discord.Member):
    await user.ban()
    print(f"Banned: {user.name} ({user.id})")



bot.run(token)