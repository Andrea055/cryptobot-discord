import discord
import requests
from discord.ext import commands
from discord.ext.commands import bot
from discord import embeds
import json
import pandas as pd
import plotly.express as px
from pycoingecko import CoinGeckoAPI

client = commands.Bot(command_prefix='.')

@client.command()
async def nanopoolergo(ctx, *, arg):
    nanopoolwork = requests.get('https://api.nanopool.org/v1/ergo/balance/' + arg)
    nanopool_data = nanopoolwork.json()
    ergobalance = str(nanopool_data['data'])
    await ctx.send(ergobalance + " ERG")

@client.command()
async def bitcoinchart(ctx):
    chart= requests.get("https://bitcoincharts.com/charts/chart.png?width=940&m=bitstampUSD&SubmitButton=Draw&r=60&i=&c=0&s=&e=&Prev=&Next=&t=T&b=&a1=&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=1&cv=0&ps=0&l=0&p=0&")
    open('chartbtc.jpg', 'wb').write(chart.content)
    await ctx.send('Thanks to bitcoincharts.com', file=discord.File('chartbtc.jpg'))

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

@client.command()
async def eth(ctx):
    cg = CoinGeckoAPI()
    eth = cg.get_coin_by_id("ethereum")
    ethvalue=eth['market_data']['current_price']['usd']
    msg=str(ethvalue)
    difficulty=requests.get("https://api.ethermine.org/networkStats")
    difjson=difficulty.json()
    dif=difjson['data']['difficulty']/1000000000000000
    msgdif = str(dif)
    await ctx.send(msg + " USD")
    await ctx.send(msgdif + " Ph")

client.run('TOKEN')
