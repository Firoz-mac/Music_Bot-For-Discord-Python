import discord
from discord.ext import commands

# use your own key here
# eg: from "page-name" import "variable"
from key import onekey

from help_cog import help_cog

from music_cog import music_cog

import asyncio

# client = commands.Bot(command_prefix="@",intents=discord.Intents.all())

# client= discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())


bot.remove_command("help")


#reaction data
emoji = '\N{THUMBS UP SIGN}'

#terminal info
@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user.name} ({bot.user.id})')
    # print('--------------------')

#when someone tag bot,

# @bot.event
# async def on_message(message):
#      if message.content.startswith('<@1195651152977600512>'):
#          await message.add_reaction(emoji)
#          print(message.author.id)
#          username = message.author.mention
#          await message.channel.send(f'hello, {username}')
    

#default command

@bot.command(name='hi')
async def info(ctx):
    username = ctx.message.author.mention
    await ctx.send(f'hello, {username}')
    
#run the bot
async def final():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(onekey)
    


asyncio.run(final())