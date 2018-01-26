import ccxt
import timeit

start_time = timeit.default_timer()
okex = ccxt.okex()
coin_dict = okex.fetchTickers()

price_dict = dict()
def getOkExDict():
    for i in coin_dict:
        base, token = i.split('/')
        if token == 'USDT':
            price = float(coin_dict[i]['last'])
            price = float("{0:.3f}".format(price))
            price_dict[base] = price

    for i in coin_dict:
        base,token = i.split('/')
        if token != 'USDT':
            if base not in price_dict:
                price = float(coin_dict[i]['last']) * float(price_dict[token])
                price = float("{0:.3f}".format(price))
                price_dict[base] = price
    return price_dict

