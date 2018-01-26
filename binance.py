import json
from fake_useragent import UserAgent
import requests
import timeit

start_time = timeit.default_timer()
ua = UserAgent(verify_ssl=False)
base_url = "http://api.binance.com"

def getBinanceCoins():
    api_coinInfo_url = base_url + "/api/v1/exchangeInfo"
    headers = {'User-Agent': ua.Safari}
    response = requests.get(api_coinInfo_url,headers=headers)

    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        return {}

def getCoinNameDict():
    coin_name_dict = dict()
    data_obj = getBinanceCoins()

    for i in data_obj['symbols']:
        key = i['symbol']
        value = i['baseAsset']
        coin_name_dict[key] = value 

    return (coin_name_dict)

def getPriceList():
    api_priceInfo_url = base_url + "/api/v3/ticker/price"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_priceInfo_url,headers=headers)
    if(response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def getBinanceDict():
    coin_dict = getCoinNameDict()

    price_list = getPriceList()

    price_dict = dict()

    for i in price_list:

        base = coin_dict[i['symbol']]
        lenbase = len(base)
        token = i['symbol'][lenbase:]
        if token == 'USDT':
            price = float(i['price'])
            price = float("{0:.3f}".format(price))
            price_dict[base] = price
        #Adding dummy value for stupid '123456':'123' entry
        price_dict['456'] = 0.0

    for i in price_list:
        base = coin_dict[i['symbol']]
        lenbase = len(base)
        token = i['symbol'][lenbase:]   
        if token != 'USDT':
            if base not in price_dict:
                price = float(i['price']) * float(price_dict[token])
                price = float("{0:.3f}".format(price))
                price_dict[base] = price

    return (price_dict)


