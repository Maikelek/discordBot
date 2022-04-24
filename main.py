import discord
import random
import requests
import asyncio
import os
from discord.ext import commands
# from keep_alive import keep_alive


#Commands are going to be called with command_prefix for example in that case it is going to be .function1
bot = commands.Bot(command_prefix='.', description="Bot")




@bot.command() #Lists all avaible functions / Not updated automatically
async def function1(ctx):
    await ctx.send("Commands are: " + "\n.function1" + "\n.function2" + "\n.function3" + "\n.function4" + "\n.function5" + "\n.function6" + "\n.function7" + "\n.function8")


@bot.command() #You can ping discord user with @user
async def function2(ctx, member:discord.Member=None):
  if member == None:
    await ctx.send(f"Example {ctx.message.author.name} example {str(random.randint(1, 30))} example")
  else:
    await ctx.send(f"example {member.mention} example {str(random.randint(1, 30))} example")



@bot.command() #You can ping author of the message || ping 1 user || ping 2 user @user1 @user2  
async def function3(ctx, member1:discord.Member=None, member2:discord.Member=None):
  if member1 == None and member2 == None:
    await ctx.send(f"{ctx.message.author.name} example {str(random.randint(1, 100))} example")
  elif member1 != None and member2 == None:
    await ctx.send(f"{member1.mention} example {str(random.randint(1, 100))} example")
  elif member1 != None and member2 != None:
    await ctx.send(f"{member1.mention} example {member2.mention} example {str(random.randint(1, 100))} example")



@bot.command() #Contacts cat API and sends picture of a cat
async def function4(ctx): 
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.send(data['file'])

@bot.command() #Chooses between 1 and 2
async def function5(ctx):
    await ctx.send(random.choice("12"))


@bot.command() #Pinging server / Works only on those servers you have access to the console
               #Ping -c 1 IP works only for Linux for Windows it is ping -n 1 IP
async def function6(ctx):
    response = os.system("ping -c 1 IP")

    if response == 0: 
        await ctx.send(random.choice("Online"))
    else:
        await ctx.send(random.choice("Not Online"))


@bot.command() #Contacts dog API and sends picture of a pembroke dog
async def function7(ctx):
    response = requests.get('https://dog.ceo/api/breed/pembroke/images/random')
    data = response.json()
    await ctx.send(data['message'])

@bot.command() #Contacts dog API and sends picture of a random dog
async def function8(ctx): 
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    await ctx.send(data['message'])






async def presence_changer(): #Function to change discord presence
    while True:
        await bot.change_presence(activity=discord.Game(name = random.choice("list[]/tuple() of your presences")))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name = random.choice("Same list[]/tuple() of your presences")))
        await asyncio.sleep(10)


@bot.event #Bot events after start
async def on_ready():

    bot.loop.create_task(presence_changer())
    print("...........")
    print("Logged as")
    print("Name: " + bot.user.name)
    print("ID: " + str(bot.user.id))
    print("...........")   





@bot.listen() #Bot is listening to the words
async def on_message(message): #He does not respond to his own words
    if message.author == bot.user:
        return

    if any(word in message.content for word in "word or {list[]/tuple()/variable}"):
      await message.channel.send("message")


#keep_alive() #If bot is hosted for example via replit then uncomment and go to keep_alive.py if not you dont need it 

#Bot Token
bot.run("BOT TOKEN from https://discord.com/developers/applications")
