import discord
import matplotlib.pyplot as plt
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
async def helpcoin(ctx):
    embed = discord.Embed(title="Help", description="All commands for this bot:")
    embed.add_field(name=".bitcoin", value="Give info about Bitcoin", inline=False)
    embed.add_field(name=".ethereum", value="Give info about Ethereum", inline=False)
    embed.add_field(name=".bnb", value="Give info about Binance Coin", inline=False)
    embed.add_field(name=".ravencoin", value="Give info about Ravencoin", inline=False)
    embed.add_field(name=".ergo", value="Give info about Ergo", inline=False)
    embed.add_field(name=".raptoreum", value="Give info about Raptoreum", inline=False)
    embed.add_field(name=".cardano", value="Give info about Cardano", inline=False)
    embed.add_field(name=".solana", value="Give info about Solana", inline=False)
    embed.add_field(name=".dogecoin", value="Give info about Dogecoin", inline=False)
    embed.add_field(name=".litecoin", value="Give info about Litecoin", inline=False)
    embed.add_field(name=".shiba", value="Give info about Shiba Inu", inline=False)
    embed.add_field(name=".ethereumclassic", value="Give info about Ethereum Classic", inline=False)
    embed.add_field(name=".monero", value="Give info about Monero", inline=False)
    embed.add_field(name=".helium", value="Give info about Helium", inline=False)
    embed.add_field(name=".ergowallet", value="Give info about an Ergo Wallet", inline=False)
    embed.add_field(name=".ethtxid", value="Give info about an Ethereum transition", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def helppool(ctx):
    embed = discord.Embed(title="Help", description="All commands about mining for this bot:")
    embed.add_field(name=".nanopoolergo+wallet", value="Give info about mining Ergo on nanopool", inline=False)
    embed.add_field(name=".ergowallet+wallet", value="Give info about Ergo wallet", inline=False)
    embed.add_field(name=".flypool+wallet", value="Give info about mining Ergo on Flypool", inline=False)
    embed.add_field(name=".nanopooleth+wallet", value="Give info about mining Ethereum on Nanopool", inline=False)
    embed.add_field(name=".twominerseth+wallet", value="Give info about mining Ethereum on 2miners pool", inline=False)
    embed.add_field(name=".ethermine+wallet", value="Give info about mining ethermine pool", inline=False)
    embed.add_field(name=".hiveon+wallet", value="Give info about mining on Hiveon pool", inline=False)
    embed.add_field(name=".nanopoolmonero+wallet", value="Give info about mining Monero on Nanopool", inline=False)
    embed.add_field(name=".nanopooletc+wallet", value="Give info about mining Ethereum Classic on Nanopool", inline=False)
    embed.add_field(name=".nanopoolrvn+wallet", value="Give info about mining Ravencoin on Nanopool", inline=False)
    embed.add_field(name=".twominersxmr+wallet", value="Give info about mining Monero on 2miners", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(title="Help", description="Help commands:")
    embed.add_field(name=".helpcoin", value="Give commands for coin", inline=False)
    embed.add_field(name=".helppool", value="Give commands for pool mining", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def nanopoolergo(ctx, *, arg):
    nanopoolwork = requests.get('https://api.nanopool.org/v1/ergo/balance/' + arg)
    nanopool_data = nanopoolwork.json()
    ergobalance = str(nanopool_data['data'])
    nanopoolhash = requests.get('https://api.nanopool.org/v1/ergo/avghashratelimited/' + arg + "/24")
    nanopool_hash = nanopoolhash.json()
    ergohash = str(nanopool_hash['data'])
    nanopoolshare = requests.get('https://api.nanopool.org/v1/ergo/shareratehistory/' + arg)
    nanopool_share = nanopoolshare.json()
    ergoshare = nanopool_share['data'][0]['shares']
    embed = discord.Embed(title="Nanopool Ergo",url="https://ergo.nanopool.org/account/" + arg, description="Mining on wallet: " + arg)
    embed.set_author(name="Nanopool Ergo mining",
                     icon_url="https://s2.coinmarketcap.com/static/img/coins/200x200/1762.png")
    embed.add_field(name="Hashrate", value=ergohash + " Mh/s", inline=True)
    embed.add_field(name="Balance", value=ergobalance + " ERG", inline=False)
    embed.add_field(name="Shares", value=ergoshare, inline=False)
    await ctx.send(embed=embed)

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
    data = requests.get("https://api.coingecko.com/api/v3/coins/binancecoin/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('bnb.png')
    cg = CoinGeckoAPI()
    bnb = cg.get_coin_by_id("binancecoin")
    bnbvalue=bnb['market_data']['current_price']['usd']
    msg=str(bnbvalue)
    embed = discord.Embed(title="Binance Coin", url="https://www.coingecko.com/en/coins/binance-coin",
                          description="Price:" + msg + " USD", color=0xfce94f)
    embed.set_author(name="Binance Coin", icon_url=bnb['image']['thumb'])
    embed.set_thumbnail(url=bnb['image']['thumb'])
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('bnb.png'))

@client.command()
async def raptoreum(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/raptoreum/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('raptoreum.png')
    cg = CoinGeckoAPI()
    rtm = cg.get_coin_by_id("raptoreum")
    rtmvalue=rtm['market_data']['current_price']['usd']
    msg=str(rtmvalue)
    embed = discord.Embed(title="Raptoreum", url="https://www.coingecko.com/it/monete/raptoreum",
                          description="Price:" + msg + " USD", color=0xc17d11)
    embed.set_author(name="Raptoreum", icon_url=rtm['image']['thumb'])
    embed.set_thumbnail(url=rtm['image']['thumb'])
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('raptoreum.png'))

@client.command()
async def cardano(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/cardano/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('cardano.png')
    cg = CoinGeckoAPI()
    ada = cg.get_coin_by_id("cardano")
    adavalue=ada['market_data']['current_price']['usd']
    msg=str(adavalue)
    embed = discord.Embed(title="Cardano", url="https://www.coingecko.com/en/coins/cardano",
                          description="Price:" + msg + " USD", color=0x3465a4)
    embed.set_author(name="Cardano", icon_url=ada['image']['thumb'])
    embed.set_thumbnail(url=ada['image']['thumb'])
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('cardano.png'))

@client.command()
async def solana(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/solana/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('solana.png')
    cg = CoinGeckoAPI()
    sol = cg.get_coin_by_id("solana")
    solvalue=sol['market_data']['current_price']['usd']
    msg=str(solvalue)
    embed = discord.Embed(title="Solana", url="https://www.coingecko.com/en/coins/solana",
                          description="Price:" + msg + " USD", color=0x75507b)
    embed.set_author(name="Solana", icon_url=sol['image']['thumb'])
    embed.set_thumbnail(url=sol['image']['thumb'])
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('solana.png'))

@client.command()
async def dogecoin(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/dogecoin/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('dogecoin.png')
    cg = CoinGeckoAPI()
    doge = cg.get_coin_by_id("dogecoin")
    dogevalue=doge['market_data']['current_price']['usd']
    msg=str(dogevalue)
    embed = discord.Embed(title="Dogecoin", url="https://www.coingecko.com/en/coins/dogecoin",
                          description="Price:" + msg + " USD", color=0xedd400)
    embed.set_author(name="Solana", icon_url=doge['image']['thumb'])
    embed.set_thumbnail(url=doge['image']['thumb'])
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('dogecoin.png'))

@client.command()
async def litecoin(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/litecoin/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('litecoin.png')
    cg = CoinGeckoAPI()
    ltc = cg.get_coin_by_id("litecoin")
    ltcvalue=ltc['market_data']['current_price']['usd']
    msg=str(ltcvalue)
    embed = discord.Embed(title="Litecoin", url="https://www.coingecko.com/en/coins/litecoin",
                          description="Price:" + msg + " USD", color=0x204a87)
    embed.set_author(name="Litecoin", icon_url=doge['image']['thumb'])
    embed.set_thumbnail(url=ltc['image']['thumb'])
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('litecoin.png'))
@client.command()
async def shiba(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/shibainu/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('shiba.png')
    cg = CoinGeckoAPI()
    shiba = cg.get_coin_by_id("shibainu")
    shibavalue=shiba['market_data']['current_price']['usd']
    msg=str(shibavalue)
    embed = discord.Embed(title="Shiba Inu", url="https://coinmarketcap.com/currencies/shiba-inu/",
                          description="Price:" + msg + " USD", color=0xce5c00)
    embed.set_author(name="Shiba Inu", icon_url=doge['image']['thumb'])
    embed.set_thumbnail(url=shiba['image']['thumb'])
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('shiba.png'))

@client.command()
async def ethereumclassic(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/ethereum-classic/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('etc.png')
    difficulty=requests.get("https://api-etc.ethermine.org/networkStats")
    difjson=difficulty.json()
    dif=difjson['data']['difficulty']/1000000000000
    msgdif = str(dif)
    cg = CoinGeckoAPI()
    etc = cg.get_coin_by_id("ethereum-classic")
    etcvalue=etc['market_data']['current_price']['usd']
    msg=str(etcvalue)
    embed = discord.Embed(title="Ethereum Classic", url="https://www.coingecko.com/en/coins/ethereum-classic",
                          description="Price:" + msg + " USD", color=0x4e9a06)
    embed.set_author(name="Ethereum Classic", icon_url=etc['image']['thumb'])
    embed.set_thumbnail(url=etc['image']['thumb'])
    embed.add_field(name="Current difficulty", value=msgdif + " TH", inline=True)
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('etc.png'))


@client.command()
async def monero(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/monero/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('monero.png')
    cg = CoinGeckoAPI()
    xmr = cg.get_coin_by_id("monero")
    xmrvalue=xmr['market_data']['current_price']['usd']
    msg=str(xmrvalue)
    embed = discord.Embed(title="Monero", url="https://www.coingecko.com/en/coins/monero",
                          description="Price:" + msg + " USD", color=0x8f5902)
    embed.set_author(name="Monero", icon_url=xmr['image']['thumb'])
    embed.set_thumbnail(url=xmr['image']['thumb'])
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('monero.png'))

@client.command()
async def helium(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/helium/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('helium.png')
    cg = CoinGeckoAPI()
    helium = cg.get_coin_by_id("helium")
    heliumvalue=helium['market_data']['current_price']['usd']
    msg=str(heliumvalue)
    embed = discord.Embed(title="Helium", url="https://www.coingecko.com/en/coins/helium",
                          description="Price:" + msg + " USD", color=0x204a87)
    embed.set_author(name="Helium", icon_url=helium['image']['thumb'])
    embed.set_thumbnail(url=helium['image']['thumb'])
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('helium.png'))
@client.command()
async def ravencoin(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/ravencoin/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('ravencoin.png')
    difficulty=requests.get("https://api-ravencoin.flypool.org/networkStats")
    difjson=difficulty.json()
    dif=difjson['data']['difficulty']/1000
    msgdif = str(dif)
    cg = CoinGeckoAPI()
    rvn = cg.get_coin_by_id("ravencoin")
    rvnvalue=rvn['market_data']['current_price']['usd']
    msg=str(rvnvalue)
    embed = discord.Embed(title="Ravencoin", url="https://www.coingecko.com/en/coins/ravencoin",
                          description="Price:" + msg + " USD", color=0xce5c00)
    embed.set_author(name="Ravencoin", icon_url=rvn['image']['thumb'])
    embed.set_thumbnail(url=rvn['image']['thumb'])
    embed.add_field(name="Current difficulty", value=msgdif + " K", inline=True)
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('ravencoin.png'))

@client.command()
async def ethereum(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('eth.png')
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
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('eth.png'))

@client.command()
async def ergo(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/ergo/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('ergo.png')
    cg = CoinGeckoAPI()
    eth = cg.get_coin_by_id("ergo")
    ethvalue=eth['market_data']['current_price']['usd']
    msg=str(ethvalue)
    difficulty=requests.get("https://api-ergo.flypool.org/networkStats")
    difjson=difficulty.json()
    dif=difjson['data']['difficulty']/100000000000
    msgdif = str(dif)
    embed = discord.Embed(title="Ergo", url="https://www.coingecko.com/en/coins/ergo", color=0x204a87)
    embed.set_author(name="Ergo", icon_url=eth['image']['thumb'])
    embed.set_thumbnail(url=eth['image']['thumb'])
    embed.add_field(name="Price", value=msg + " USD", inline=True)
    embed.add_field(name="Current difficulty", value=msgdif + " PH", inline=True)
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('ergo.png'))

@client.command()
async def ergowallet(ctx, *, arg):
    ergoexp = requests.get('https://api.ergoplatform.com/api/v1/addresses/' + arg + '/balance/total')
    egoexpdate = ergoexp.json()
    ergobalance = str(egoexpdate['confirmed']['nanoErgs'])
    await ctx.send(ergobalance + " ERG")


@client.command()
async def flypoolergo(ctx, *, arg):
    flypoolapi = requests.get('https://api-ergo.flypool.org/miner/" + arg + "/dashboard')
    flyerg = flypoolapi.json()
    ergobalance = str(flyerg['data']['currentStatistics']['unpaid'] / 1000000000)
    await ctx.send(ergobalance + " ERG")

@client.command()
async def flypoolrvn(ctx, *, arg):
    flypoolapi = requests.get('https://api-ravencoin.flypool.org/miner/" + arg + "/dashboard')
    flyerg = flypoolapi.json()
    ergobalance = str(flyerg['data']['currentStatistics']['unpaid'] / 1000000000)
    await ctx.send(ergobalance + " RVN")

@client.command()
async def flypooleth(ctx, *, arg):
    flypoolapi = requests.get('https://api.ethermine.org/miner/" + arg + "/dashboard')
    flyerg = flypoolapi.json()
    ergobalance = str(flyerg['data']['currentStatistics']['unpaid'] / 1000000000)
    await ctx.send(ergobalance + " ETH")

@client.command()
async def flypoolzcash(ctx, *, arg):
    flypoolapi = requests.get('https://api-zcash.flypool.org/miner/" + arg + "/dashboard')
    flyerg = flypoolapi.json()
    ergobalance = str(flyerg['data']['currentStatistics']['unpaid'] / 1000000000)
    await ctx.send(ergobalance + " Zcash")

@client.command()
async def flypooletc(ctx, *, arg):
    flypoolapi = requests.get('https://api-etc.ethermine.org/miner/" + arg + "/dashboard')
    flyerg = flypoolapi.json()
    ergobalance = str(flyerg['data']['currentStatistics']['unpaid'] / 1000000000)
    await ctx.send(ergobalance + " ETC")

@client.command()
async def flypoolbeam(ctx, *, arg):
    flypoolapi = requests.get('https://api-beam.flypool.org/miner/" + arg + "/dashboard')
    flyerg = flypoolapi.json()
    ergobalance = str(flyerg['data']['currentStatistics']['unpaid'] / 1000000000)
    await ctx.send(ergobalance + " BEAM")

@client.command()
async def nanopooleth(ctx, *, arg):
    nanopooleth = requests.get('https://api.nanopool.org/v1/eth/balance/' + arg)
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['data'])
    nanopoolhash = requests.get('https://api.nanopool.org/v1/eth/balance/avghashratelimited/' + arg + "/24")
    nanopool_hash = nanopoolhash.json()
    ergohash = str(nanopool_hash['data'])
    nanopoolshare = requests.get('https://api.nanopool.org/v1/eth/balance//shareratehistory/' + arg)
    nanopool_share = nanopoolshare.json()
    ergoshare = nanopool_share['data'][0]['shares']
    embed = discord.Embed(title="Nanopool Ethereum", url="https://eth.nanopool.org/account/" + arg,
                          description="Mining on wallet: " + arg)
    embed.set_author(name="Nanopool Ethereum mining",
                     icon_url="https://s2.coinmarketcap.com/static/img/coins/200x200/1762.png")
    embed.add_field(name="Hashrate", value=ergohash + " Mh/s", inline=True)
    embed.add_field(name="Balance", value=ergobalance + " ETH", inline=False)
    embed.add_field(name="Shares", value=ergoshare, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def twominerseth(ctx, *, arg):
    nanopooleth = requests.get('https://eth.2miners.com/api/accounts/' + arg)
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['stats']['paid'] / 1000000000)
    ethshare = str(nanopoolapi['stats']['lastShare'])
    ethhash = str(nanopoolapi['currentHashrate'] / 1000000)
    ethworker = str(nanopoolapi['workersOnline'])
    embed = discord.Embed(title="2miners Ethereum", url="https://eth.2miners.com/account/" + arg,
                          description="Mining on wallet: " + arg)
    embed.set_author(name="2miners Ethereum mining",
                     icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/1200px-Ethereum-icon-purple.svg.png")
    embed.add_field(name="Hashrate", value=ethhash + " Mh/s", inline=True)
    embed.add_field(name="Balance", value=ethbalance + " Eth", inline=False)
    embed.add_field(name="Shares", value=ethshare, inline=False)
    embed.add_field(name="Online worker", value=ethworker, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ethermine(ctx, *, arg):
    nanopooleth = requests.get('https://api.ethermine.org/miner/' + arg + "/dashboard")
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['data']['currentStatistics']['unpaid'] / 1000000000000000000)

    nanopooleth = requests.get('https://api.ethermine.org/miner/' + arg + "/dashboard")
    nanopoolapi = nanopooleth.json()
    ethshare = str(nanopoolapi['data']['currentStatistics']['validShares'])

    nanopooleth = requests.get('https://api.ethermine.org/miner/' + arg + "/dashboard")
    nanopoolapi = nanopooleth.json()
    ethhash = str(nanopoolapi['data']['currentStatistics']['reportedHashrate'] / 1000000)

    embed = discord.Embed(title="Ethermine Ethereum",
                          description="Mining on wallet: " + arg)
    embed.set_author(name="Ethermine Ethereum mining",
                     icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/1200px-Ethereum-icon-purple.svg.png")
    embed.add_field(name="Hashrate", value=ethhash + " Mh/s", inline=True)
    embed.add_field(name="Balance", value=ethbalance + " Eth", inline=False)
    embed.add_field(name="Shares", value=ethshare, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def hiveon(ctx, *, arg):
    hiveeth = requests.get('https://hiveon.net/api/v1/stats/miner/walletAddress123/' + arg + "ETH/billing-acc")
    hiveapi = hiveeth.json()
    bilance = (hiveapi['succeedPayouts'] + hiveapi['pendingPayouts']) / 1000000000000000000
    ethbalance = str(bilance)
    await ctx.send(ethbalance + " ETH")

@client.command()
async def nanopoolmonero(ctx, *, arg):
    nanopooleth = requests.get('https://api.nanopool.org/v1/xmr/balance/' + arg)
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['data'])
    nanopoolhash = requests.get('https://api.nanopool.org/v1/xmr/balance/avghashratelimited/' + arg + "/24")
    nanopool_hash = nanopoolhash.json()
    ergohash = str(nanopool_hash['data'])
    nanopoolshare = requests.get('https://api.nanopool.org/v1/xmr/balance/shareratehistory/' + arg)
    nanopool_share = nanopoolshare.json()
    ergoshare = nanopool_share['data'][0]['shares']
    embed = discord.Embed(title="Nanopool Monero", url="https://xmr.nanopool.org/account/" + arg,
                          description="Mining on wallet: " + arg)
    embed.set_author(name="Nanopool Monero mining",
                     icon_url="https://s2.coinmarketcap.com/static/img/coins/64x64/328.png")
    embed.add_field(name="Hashrate", value=ergohash + " Mh/s", inline=True)
    embed.add_field(name="Balance", value=ergobalance + " XMR", inline=False)
    embed.add_field(name="Shares", value=ergoshare, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def nanopoolrvn(ctx, *, arg):
    nanopooleth = requests.get('https://api.nanopool.org/v1/rvn/balance/' + arg)
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['data'])
    nanopoolhash = requests.get('https://api.nanopool.org/v1/rvn/balance/avghashratelimited/' + arg + "/24")
    nanopool_hash = nanopoolhash.json()
    ergohash = str(nanopool_hash['data'])
    nanopoolshare = requests.get('https://api.nanopool.org/v1/rvn/balance/shareratehistory/' + arg)
    nanopool_share = nanopoolshare.json()
    ergoshare = nanopool_share['data'][0]['shares']
    embed = discord.Embed(title="Nanopool Ravencoin", url="https://rvn.nanopool.org/account/" + arg,
                          description="Mining on wallet: " + arg)
    embed.set_author(name="Nanopool Ravencoin mining",
                     icon_url="https://s2.coinmarketcap.com/static/img/coins/64x64/2577.png")
    embed.add_field(name="Hashrate", value=ergohash + " Mh/s", inline=True)
    embed.add_field(name="Balance", value=ergobalance + " RVN", inline=False)
    embed.add_field(name="Shares", value=ergoshare, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def nanopooletc(ctx, *, arg):
    nanopooleth = requests.get('https://api.nanopool.org/v1/etc/balance/' + arg)
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['data'])
    nanopoolhash = requests.get('https://api.nanopool.org/v1/etc/balance/avghashratelimited/' + arg + "/24")
    nanopool_hash = nanopoolhash.json()
    ergohash = str(nanopool_hash['data'])
    nanopoolshare = requests.get('https://api.nanopool.org/v1/etc/balance/shareratehistory/' + arg)
    nanopool_share = nanopoolshare.json()
    ergoshare = nanopool_share['data'][0]['shares']
    embed = discord.Embed(title="Nanopool Ethereum Classic", url="https://etc.nanopool.org/account/" + arg,
                          description="Mining on wallet: " + arg)
    embed.set_author(name="Nanopool Ethereum Classic mining",
                     icon_url="https://s2.coinmarketcap.com/static/img/coins/64x64/1321.png")
    embed.add_field(name="Hashrate", value=ergohash + " Mh/s", inline=True)
    embed.add_field(name="Balance", value=ergobalance + " ETC", inline=False)
    embed.add_field(name="Shares", value=ergoshare, inline=False)
    await ctx.send(embed=embed)


@client.command()
async def twominersxmr(ctx, *, arg):
    nanopooleth = requests.get('https://xmr.2miners.com/api/accounts/' + arg)
    nanopoolapi = nanopooleth.json()
    ethbalance = str(nanopoolapi['stats']['paid'] / 1000000000)
    await ctx.send(ethbalance + " XMR")

@client.command()
async def ethtxid(ctx, *, arg):
    status= requests.get("https://api.etherscan.io/api?module=transaction&action=gettxreceiptstatus&txhash=" + arg + "&apikey=APIKEY")
    statusmsg=status.json()
    await ctx.send("Your transition is" + statusmsg['message'])

@client.command()
async def ton(ctx):
    data = requests.get("https://api.coingecko.com/api/v3/coins/the-open-network/market_chart?vs_currency=usd&days=7d")
    d = data.json()
    df = pd.DataFrame(d['prices'])
    df.plot(x=0, y=1)
    plt.savefig('ton.png')
    cg = CoinGeckoAPI()
    ton = cg.get_coin_by_id("the-open-network")
    ethvalue=ton['market_data']['current_price']['usd']
    msg=str(ethvalue)
    difficulty=requests.get("https://api-ergo.flypool.org/networkStats")
    difjson=difficulty.json()
    dif=difjson['data']['difficulty']/100000000000
    msgdif = str(dif)
    embed = discord.Embed(title="TON", url="https://www.coingecko.com/en/coins/the-open-network", color=0x204a87)
    embed.set_author(name="TON", icon_url=ton['image']['thumb'])
    embed.set_thumbnail(url=ton['image']['thumb'])
    embed.add_field(name="Price", value=msg + " USD", inline=True)
    embed.add_field(name="Current difficulty", value=msgdif + " PH", inline=True)
    await ctx.send(embed=embed)
    await ctx.send('Thanks CoinGeckoAPI', file=discord.File('ton.png'))



client.run('TOKEN')
