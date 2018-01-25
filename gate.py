import json
from fake_useragent import UserAgent
import requests

ua = UserAgent(verify_ssl=False)
api_url = "http://data.gate.io/api2/1"

def getGateCoins():
    api_gate_url = api_url + "/tickers"
    headers = {'User-Agent': ua.Safari}
    response = requests.get(api_gate_url,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
    

def getGateDict():
    coin_list = getGateCoins()

    price_dict = dict()

    for i in coin_list:
        base, token = i.split('_')
        if token == 'usdt':
            price_dict[base] = coin_list[i]['last']

    for i in coin_list:
        base,token = i.split('_')
        if token != 'usdt':
            if base not in price_dict:
                price = float(price_dict[token]) * float(coin_list[i]['last'])
                #Do price round off
                price_dict[base] = price

    return (price_dict)


print (getGateDict())

