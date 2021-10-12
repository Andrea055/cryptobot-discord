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
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

@client.event                 #message connect!
async def on_ready():
    print("Bot is ready")

@client.command()
async def nanopoolergo(ctx, *, arg):
    nanopoolwork = requests.get('https://api.nanopool.org/v1/ergo/balance/' + arg)
    nanopool_data = nanopoolwork.json()
    ergobalance = str(nanopool_data['data'])
    await ctx.send(ergobalance + " ERG")

@client.command()
async def bitcoin(ctx):
    cg = CoinGeckoAPI()
    btc = cg.get_coin_by_id("bitcoin")
    btcvalue=btc['market_data']['current_price']['usd']
    msg=str(btcvalue)
    chart= requests.get("https://bitcoincharts.com/charts/chart.png?width=940&m=bitstampUSD&SubmitButton=Draw&r=60&i=&c=0&s=&e=&Prev=&Next=&t=T&b=&a1=&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=1&cv=0&ps=0&l=0&p=0&")
    open('chartbtc.jpg', 'wb').write(chart.content)
    embed = discord.Embed(title="Bitcoin", url="https://www.coingecko.com/en/coins/bitcoin",
                          description="Price:" + msg + " USD", color=0xfcaf3e)
    embed.set_author(name="Bitcoin", icon_url="https://s2.coinmarketcap.com/static/img/coins/200x200/1.png")
    embed.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/200x200/1.png")
    embed.add_field(name="Chart:", value="👇", inline=True)
    await ctx.send(embed=embed)
    await ctx.send('Thanks to bitcoincharts.com', file=discord.File('chartbtc.jpg'))

@client.command()
async def bnb(ctx):
    cg = CoinGeckoAPI()
    bnb = cg.get_coin_by_id("binancecoin")
    bnbvalue=bnb['market_data']['current_price']['usd']
    msg=str(bnbvalue)
    embed = discord.Embed(title="Binance Coin", url="https://www.coingecko.com/en/coins/binance-coin",
                          description="Price:" + msg + " USD", color=0xfce94f)
    embed.set_author(name="Binance Coin", icon_url=bnb['image']['thumb'])
    embed.set_thumbnail(url=bnb['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def raptoreum(ctx):
    cg = CoinGeckoAPI()
    rtm = cg.get_coin_by_id("raptoreum")
    rtmvalue=rtm['market_data']['current_price']['usd']
    msg=str(rtmvalue)
    embed = discord.Embed(title="Raptoreum", url="https://www.coingecko.com/it/monete/raptoreum",
                          description="Price:" + msg + " USD", color=0xc17d11)
    embed.set_author(name="Raptoreum", icon_url=rtm['image']['thumb'])
    embed.set_thumbnail(url=rtm['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def cardano(ctx):
    cg = CoinGeckoAPI()
    ada = cg.get_coin_by_id("cardano")
    adavalue=ada['market_data']['current_price']['usd']
    msg=str(adavalue)
    embed = discord.Embed(title="Cardano", url="https://www.coingecko.com/en/coins/cardano",
                          description="Price:" + msg + " USD", color=0x3465a4)
    embed.set_author(name="Cardano", icon_url=ada['image']['thumb'])
    embed.set_thumbnail(url=ada['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def solana(ctx):
    cg = CoinGeckoAPI()
    sol = cg.get_coin_by_id("solana")
    solvalue=sol['market_data']['current_price']['usd']
    msg=str(solvalue)
    embed = discord.Embed(title="Solana", url="https://www.coingecko.com/en/coins/solana",
                          description="Price:" + msg + " USD", color=0x75507b)
    embed.set_author(name="Solana", icon_url=sol['image']['thumb'])
    embed.set_thumbnail(url=sol['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def dogecoin(ctx):
    cg = CoinGeckoAPI()
    doge = cg.get_coin_by_id("dogecoin")
    dogevalue=doge['market_data']['current_price']['usd']
    msg=str(dogevalue)
    embed = discord.Embed(title="Dogecoin", url="https://www.coingecko.com/en/coins/dogecoin",
                          description="Price:" + msg + " USD", color=0xedd400)
    embed.set_author(name="Solana", icon_url=doge['image']['thumb'])
    embed.set_thumbnail(url=doge['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def litecoin(ctx):
    cg = CoinGeckoAPI()
    ltc = cg.get_coin_by_id("litecoin")
    ltcvalue=ltc['market_data']['current_price']['usd']
    msg=str(ltcvalue)
    embed = discord.Embed(title="Litecoin", url="https://www.coingecko.com/en/coins/litecoin",
                          description="Price:" + msg + " USD", color=0x204a87)
    embed.set_author(name="Litecoin", icon_url=doge['image']['thumb'])
    embed.set_thumbnail(url=ltc['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def shiba(ctx):
    cg = CoinGeckoAPI()
    shiba = cg.get_coin_by_id("shibainu")
    shibavalue=shiba['market_data']['current_price']['usd']
    msg=str(shibavalue)
    embed = discord.Embed(title="Shiba Inu", url="https://coinmarketcap.com/currencies/shiba-inu/",
                          description="Price:" + msg + " USD", color=0xce5c00)
    embed.set_author(name="Shiba Inu", icon_url=doge['image']['thumb'])
    embed.set_thumbnail(url=shiba['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def etc(ctx):
    cg = CoinGeckoAPI()
    etc = cg.get_coin_by_id("ethereumclassic")
    etcvalue=etc['market_data']['current_price']['usd']
    msg=str(etcvalue)
    embed = discord.Embed(title="Ethereum Classic", url="https://www.coingecko.com/en/coins/ethereum-classic",
                          description="Price:" + msg + " USD", color=0x4e9a06)
    embed.set_author(name="Ethereum Classic", icon_url=etc['image']['thumb'])
    embed.set_thumbnail(url=etc['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def monero(ctx):
    cg = CoinGeckoAPI()
    xmr = cg.get_coin_by_id("monero")
    xmrvalue=xmr['market_data']['current_price']['usd']
    msg=str(xmrvalue)
    embed = discord.Embed(title="Monero", url="https://www.coingecko.com/en/coins/monero",
                          description="Price:" + msg + " USD", color=0x8f5902)
    embed.set_author(name="Monero", icon_url=xmr['image']['thumb'])
    embed.set_thumbnail(url=xmr['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def helium(ctx):
    cg = CoinGeckoAPI()
    helium = cg.get_coin_by_id("helium")
    heliumvalue=helium['market_data']['current_price']['usd']
    msg=str(heliumvalue)
    embed = discord.Embed(title="Helium", url="https://www.coingecko.com/en/coins/helium",
                          description="Price:" + msg + " USD", color=0x204a87)
    embed.set_author(name="Helium", icon_url=helium['image']['thumb'])
    embed.set_thumbnail(url=helium['image']['thumb'])
    await ctx.send(embed=embed)

@client.command()
async def ravencoin(ctx):
    cg = CoinGeckoAPI()
    rvn = cg.get_coin_by_id("ravencoin")
    rvnvalue=rvn['market_data']['current_price']['usd']
    msg=str(rvnvalue)
    embed = discord.Embed(title="Ravencoin", url="https://www.coingecko.com/en/coins/ravencoin",
                          description="Price:" + msg + " USD", color=0xce5c00)
    embed.set_author(name="Ravencoin", icon_url=rvn['image']['thumb'])
    embed.set_thumbnail(url=rvn['image']['thumb'])
    await ctx.send(embed=embed)

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
    embed = discord.Embed(title="Ethereum", url="https://www.coingecko.com/it/monete/ethereum", color=0x204a87)
    embed.set_author(name="Ethereum", icon_url=eth['image']['thumb'])
    embed.set_thumbnail(url=eth['image']['thumb'])
    embed.add_field(name="Price", value=msg + " USD", inline=True)
    embed.add_field(name="Current difficulty", value=msgdif + " PH", inline=True)
    await ctx.send(embed=embed)

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
