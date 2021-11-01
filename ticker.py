import time
from pycoingecko import CoinGeckoAPI

starttime = time.time()

# Set variables to access later
crypto_id = ['ethereum','hoge-finance']
crypto_coin = ['ETH','HOGE']
functions = ['usd']
results = []

# Add on your own
stored_amounts = []

while True:

    cg = CoinGeckoAPI()
    for coin in range(len(crypto_id)):

        API_return = cg.get_price(ids=crypto_id[coin], vs_currencies='usd')
        results.append(API_return[crypto_id[coin]]['usd'])

    for coin in range(len(results)):
        print(crypto_coin[coin] + "\t" + str(round(results[coin]*stored_amounts[coin],2)) + "\t" + str(results[coin]))

    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
    cg=''
    results=[]
