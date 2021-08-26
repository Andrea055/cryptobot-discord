import requests
import json
import os
import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import embeds
response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin')
json_data = response.json()

client = commands.Bot(command_prefix='.')    #define bot prefix



@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

@client.command()                                       # wide command and processing
async def nanopoolergo(ctx, *, arg):
    nanopoolwork = requests.get('https://api.nanopool.org/v1/ergo/user/' + arg)
    nanopool_data = nanopoolwork.json()
    worker = requests.get('https://api.nanopool.org/v1/ergo/workers' + arg)
    worker_data = worker.json()
    embedVar = discord.Embed(title="Ergo NanoPool Info", color=0x00ff00)
    embedVar.set_image(url="https://s2.coinmarketcap.com/static/img/coins/200x200/1762.png")
    embedVar.add_field(name="Description", value=nanopool_data['data'], inline=False)
    embedVar.add_field(name="Ratings", value=worker_data['data'][0]['id'], inline=False)
    await ctx.send(embed=embedVar)



client.run('TOKEN')




