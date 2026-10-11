#English/Inglês 
#this code is my FrutigerEcoBot that is a Discord chat bot you can use this code AS inspiration or help with something if you encounter any problems if your own code if you're going to use this code don't just copy and paste it this is only for making a first chat bot or the basic starting code for chatbot
#Spanish/Español
#Este código corresponde a mi FrutigerEcoBot, un bot de chat para Discord. Puedes utilizarlo como inspiración o como ayuda si te surge algún problema con tu propio código; sin embargo, no te limites a copiarlo y pegarlo, ya que está pensado únicamente para crear un primer bot de chat o para servir como base inicial.
import os
import discord
import random
from discord.ext import commands
print("bot.py started")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="Hey Eco ", intents=intents)

@bot.event
async def on_ready():
    print(f"FrutigerEcoBot is ready! {bot.user.name}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello! I'm FrutigerEcoBot you can call me Eco! :D {ctx.author.mention}")

@bot.command()
async def images(ctx):
    images = os.listdir("image")
    images_send = random.choice(images)
    
    with open(f"image/{images_send}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def HowToReduceWaste(ctx):
    await ctx.send(random.choice(["One way to reduce waste is to your clean home once like every 1 week and a half or every 2 weeks", "One way to reduce waste is when you are on a walk and you see trash on the ground pick it up and put it in a bin or a recycle bin."]))    
@bot.command()
async def video(ctx):
    videos = os.listdir("MP4 videos")
    video_to_send = random.choice(videos)
    with open(f"MP4 videos/{video_to_send}", "rb") as f:
        video = discord.File(f)
    await ctx.send(file=video)

print("bot.py started")

bot.run("")


    


