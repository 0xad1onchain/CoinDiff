import ccxt
import timeit

start_time = timeit.default_timer()
kucoin = ccxt.kucoin()
coin_dict = kucoin.fetchTickers()

price_dict = dict()
def getKuCoinDict():
    for i in coin_dict:
        base, token = i.split('/')
        if token == 'USDT':
            price_dict[base] = coin_dict[i]['last']

    for i in coin_dict:
        base,token = i.split('/')
        if token != 'USDT':
            if base not in price_dict:
                price_dict[base] = float(coin_dict[i]['last']) * float(price_dict[token])
    return price_dict

print (getKuCoinDict())
print (timeit.default_timer() - start_time)