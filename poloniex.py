import json
from fake_useragent import UserAgent
import requests
import timeit

start_time = timeit.default_timer()
ua = UserAgent(verify_ssl=False)
api_url = "https://poloniex.com/public?command=returnTicker"

def getPoloniexCoins():
    headers = {'User-Agent': ua.Safari}
    response = requests.get(api_url,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        return {}
    

def getPoloniexDict():
    coin_list = getPoloniexCoins()

    price_dict = dict()

    for i in coin_list:
        base, token = i.split('_')
        base = base.upper()
        token = token.upper()
        if token == 'USDT':
            price_dict[base] = float(coin_list[i]['last'])

    for i in coin_list:
        base,token = i.split('_')
        base = base.upper()
        token = token.upper()
        if token != 'USDT':
            if base not in price_dict:
                price = float(price_dict[token]) * float(coin_list[i]['last'])
                #Do price round off
                price_dict[base] = price

    return (price_dict)




