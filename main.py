import discord
import requests
from discord.ext import commands
from discord.ext.commands import bot
from discord import embeds
import json

client = commands.Bot(command_prefix='.')

@client.command()
async def nanopoolergo(ctx, *, arg):
    nanopoolwork = requests.get('https://api.nanopool.org/v1/ergo/balance/' + arg)
    nanopool_data = nanopoolwork.json()
    await ctx.send(nanopool_data['data'])


@client.command()
async def ergowallet(ctx, *, arg):
    ergoexp = requests.get('https://api.ergoplatform.com/api/v1/addresses/' + arg + '/balance/total')
    egoexpdate = ergoexp.json()
    await ctx.send(egoexpdate['confirmed']['nanoErgs'])

@client.command()
async def flypool(ctx, *, arg):
    flypoolapi = requests.get('https://api-ergo.flypool.org/miner/" + arg + "/dashboard')
    flyerg = flypoolapi.json()
    await ctx.send(flyerg['data']['currentStatistics']['unpaid'] / 1000000000)

@client.command()
async def nanopooleth(ctx, *, arg):
    nanopooleth = requests.get('https://api.nanopool.org/v1/eth/balance/' + arg)
    nanopoolapi = nanopooleth.json()
    await ctx.send("Pool bilance" + nanopoolapi['data'])

@client.command()
async def twominerseth(ctx, *, arg):
    nanopooleth = requests.get('https://eth.2miners.com/api/accounts/' + arg)
    nanopoolapi = nanopooleth.json()
    await ctx.send("Pool bilance" + nanopoolapi['stats']['paid'] / 1000000000)

@client.command()
async def ethermine(ctx, *, arg):
    nanopooleth = requests.get('https://api.ethermine.org/miner/' + arg + "/dashboard")
    nanopoolapi = nanopooleth.json()
    await ctx.send("Pool bilance" + nanopoolapi['data']['currentStatistics']['unpaid'] / 1000000000000000000)

@client.command()
async def hiveon(ctx, *, arg):
    hiveeth = requests.get('https://hiveon.net/api/v1/stats/miner/walletAddress123/' + wallet + "ETH/billing-acc")
    hiveapi = hiveeth.json()
    bilance = (hiveapi['succeedPayouts'] + hiveapi['pendingPayouts']) / 1000000000000000000
    await ctx.send("Pool bilance" + bilance)

client.run('TOKEN')
