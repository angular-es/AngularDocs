import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re
# Ask for the token please 
TOKEN = ''
# Prefix to call bot
bot = commands.Bot(command_prefix='$', description="This is a Helper Bot")
# Exmple command
@bot.command()
async def x(ctx):
    await ctx.send('y')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="This is a Angular Docs Helper", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://angular.io/assets/images/logos/angular/angular.svg")

    await ctx.send(embed=embed)

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Angular", type='1'))
    print('Always Remenber the banana is in the box')
# I think in this part we can make the docs , if anyone knows another way welcome
@bot.listen()
async def on_message(message):
    if "features" in message.content.lower():
        embedVar = discord.Embed(title="Features and benefits", description="All angular things", color=discord.Color.red())
        embedVar.add_field(name="Progressive Web Apps", value="1", inline=False)
        embedVar.add_field(name="Native", value="2", inline=False)
        embedVar.add_field(name="Desktop", value="3", inline=False)
        embedVar.add_field(name="For More Visit", value=f"https://angular.io/features",inline=False)
        embedVar.set_thumbnail(url="https://angular.io/assets/images/logos/angular/angular.svg")

        await message.channel.send(embed=embedVar)

bot.run(TOKEN)