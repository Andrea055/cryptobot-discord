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
    ergobalance = str(nanopool_data['data'])
    await ctx.send(ergobalance + " ERG")


@client.command()
async def ergowallet(ctx, *, arg):
    ergoexp = requests.get('https://api.ergoplatform.com/api/v1/addresses/' + arg + '/balance/total')
    egoexpdate = ergoexp.json()
    ergobalance = str(egoexpdate['confirmed']['nanoErgs'])
    await ctx.send(ergobalance + " ERG")


@client.command()
async def flypool(ctx, *, arg):
    flypoolapi = requests.get('https://api-ergo.flypool.org/miner/" + arg + "/dashboard')
    flyerg = flypoolapi.json()
    ergobalance = str(flyerg['data']['currentStatistics']['unpaid'] / 1000000000)
    await ctx.send(ergobalance + " ERG")

@client.command()
async def nanopooleth(ctx, *, arg):
    nanopooleth = requests.get('https://api.nanopool.org/v1/eth/balance/' + arg)
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['data'])
    await ctx.send(ethbalance + " ETH")

@client.command()
async def twominerseth(ctx, *, arg):
    nanopooleth = requests.get('https://eth.2miners.com/api/accounts/' + arg)
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['stats']['paid'] / 1000000000)
    await ctx.send(ethbalance + " ETH")

@client.command()
async def ethermine(ctx, *, arg):
    nanopooleth = requests.get('https://api.ethermine.org/miner/' + arg + "/dashboard")
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['data']['currentStatistics']['unpaid'] / 1000000000000000000)
    await ctx.send(ethbalance + " ETH")

@client.command()
async def hiveon(ctx, *, arg):
    hiveeth = requests.get('https://hiveon.net/api/v1/stats/miner/walletAddress123/' + arg + "ETH/billing-acc")
    hiveapi = hiveeth.json()
    bilance = (hiveapi['succeedPayouts'] + hiveapi['pendingPayouts']) / 1000000000000000000
    ethbalance = str(bilance)
    await ctx.send(ethbalance + " ETH")

@client.command()
async def nanopoolmonero(ctx, *, arg):
    xmr = requests.get('https://api.nanopool.org/v1/xmr/balance/' + arg)
    xmrapi = xmr.json()
    ethbalance = str(xmrapi['data'])
    await ctx.send(ethbalance + " XMR")

@client.command()
async def twominersxmr(ctx, *, arg):
    nanopooleth = requests.get('https://xmr.2miners.com/api/accounts/' + arg)
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['stats']['paid'] / 1000000000)
    await ctx.send(ethbalance + " XMR")

client.run('TOKEN')
