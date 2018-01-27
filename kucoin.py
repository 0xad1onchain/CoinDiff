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
            if (coin_dict[i]['last'] is not None):
                price = float(coin_dict[i]['last'])
                price = float("{0:.3f}".format(price))
                price_dict[base] = price

    for i in coin_dict:
        base,token = i.split('/')
        if token != 'USDT':
            if base not in price_dict:
                if (coin_dict[i]['last'] is not None and price_dict[token] is not None):
                    price = float(coin_dict[i]['last']) * float(price_dict[token])
                    price = float("{0:.3f}".format(price))
                    price_dict[base] = price
    return price_dict

