import json
from fake_useragent import UserAgent
import requests

api_url = "https://poloniex.com/public"
ua = UserAgent(verify_ssl=False)

def getPoloniexCoins():
    
    api_gate_url = api_url + "?command=returnTicker"
    headers = {'User-Agent': ua.Safari}
    response = requests.get(api_gate_url,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        return None



def getPoloniexDict()
    coin_list = getPoloniexCoins()

    price_dict = dict()

    for i in coin_list:
        token, base = i.split('_')
        if token == 'USDT':
            price_dict[base] = coin_list[i]['last']
    for i in coin_list:
        token, base = i.split('_')
        if token != 'USDT':
            if base not in price_dict:
                price_dict[base] = float(coin_list[i]['last']) * float(price_dict[token])
    

