import json
import requests
import ccxt


def getPoloniexCoins():
    polo = ccxt.poloniex()
    coin_dict = polo.fetchTickers()
    return coin_dict


def getPoloniexDict():
    coin_list = getPoloniexCoins()
    print(type(coin_list))
    price_dict = dict()

    for i in coin_list:
        base, token = i.split('/')
        if token == 'USDT':
            price_dict[base] = float(coin_list[i]['last'])
    for i in coin_list:
        base, token = i.split('/')
        if token != 'USDT':
            if base not in price_dict:
                price_dict[base] = float(coin_list[i]['last']) * float(price_dict[token])

    return price_dict
    
