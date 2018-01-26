'''
General format for imported exchanges:
exchangeDict = {
    'COIN': value_in_USDT, ...
}
'''

import binance
import gate
import kucoin
import okex
import poloniex
import operator

exchanges = {'Binance', 'Gate.IO', 'OKEX', 'KuCoin', 'Poloniex'}
finalPriceDict = dict()

def initialize():
    global finalPriceDict
    finalPriceDict = {}
    binanceDict = binance.getBinanceDict()
    kuCoinDict = kucoin.getKuCoinDict()
    gateDict = gate.getGateDict()
    okexDict = okex.getOkExDict()
    #poloniexDict = poloniex.getPoloniexDict()
    #Add more exchanges here

    '''
    IMPORTANT: Names of exchanges entered here should be same as ones in the list 'exchanges'
    '''
    addInDict(gateDict, 'Gate.IO')
    addInDict(okexDict, 'OKEX')
    addInDict(binanceDict, 'Binance')
    addInDict(kuCoinDict, 'KuCoin')
    #addInDict(poloniexDict, 'Poloniex')
    #Add more exchanges here

    del binanceDict
    del kuCoinDict
    del okexDict
    #del poloniexDict
    del gateDict

def addInDict(exchangeDict, exchangeName):
    for i in exchangeDict:
        if i not in finalPriceDict:
            finalPriceDict[i] = dict()
            finalPriceDict[i][exchangeName] = exchangeDict[i]
        else:
            finalPriceDict[i][exchangeName] = exchangeDict[i]

def getDiff():

    initialize()
    global finalPriceDict
    tempDict = dict()
    for i in finalPriceDict:
        if len(finalPriceDict[i]) != 1:
            tempDict[i] = finalPriceDict[i]

    finalPriceDict = tempDict
    del tempDict

    statDict = dict()
    percDict = dict()
    for i in finalPriceDict:
        statDict[i] = dict()
        statDict[i]['max'] = dict()
        statDict[i]['min'] = dict()
        statDict[i]['diff'] = dict()
        statDict[i]['max']['exchange'] = max(finalPriceDict[i].keys(), key=lambda k: finalPriceDict[i][k])
        statDict[i]['max']['value'] = finalPriceDict[i][statDict[i]['max']['exchange']]
        statDict[i]['min']['exchange'] = min(finalPriceDict[i].keys(), key=lambda k: finalPriceDict[i][k])
        statDict[i]['min']['value'] = finalPriceDict[i][statDict[i]['min']['exchange']]
        statDict[i]['diff']['value'] = statDict[i]['max']['value'] - statDict[i]['min']['value']
        statDict[i]['diff']['perc'] = statDict[i]['diff']['value']*100/statDict[i]['min']['value']
        percDict[i] = statDict[i]['diff']['perc']

    for i in finalPriceDict:
        for j in exchanges:
            if j not in finalPriceDict[i]:
                finalPriceDict[i][j] = -1


    outputDict = dict()
    outputDict['prices'] = finalPriceDict
    outputDict['stats'] = statDict
    outputDict['perc'] = percDict
    

    return (outputDict)

