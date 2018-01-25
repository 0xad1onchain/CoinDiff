import ccxt

okex = ccxt.okex()
coin_dict = okex.fetchTickers()

price_dict = dict()
def getOkExDict():
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

print (len(getOkExDict()))
