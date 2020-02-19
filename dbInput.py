from pymongo import MongoClient
import requests
import threading

def tirarOPontinho(oldJson):  # Evitar problemas na hora de registrar no MongoDB
    x = ''
    newJson = {}
    for timestamp in oldJson:
        newJson[timestamp] = {}
        for n in oldJson[timestamp]:
            if n == '1. open':
                 x = 'open'
            elif n == '2. high':
                x = 'high'
            elif n == '3. low':
                x = 'low'
            elif n == '4. close':
                x = 'close'
            elif n == '5. volume':
                x = 'volume'
            newJson[timestamp][x] = oldJson[timestamp][n]

    return newJson


def salvar_json_no_banco(nome_do_ativo, indicador, arquivo):
    client = MongoClient()
    db = client.get_database('banco_de_dados')
    collection = db.get_collection('collect')

    # Para limpar os dados:
    # db.drop_collection('banco_de_dados')

    for key, value in arquivo.items():
        dado = {
            'nome do ativo': nome_do_ativo,
            'indicador': indicador,
            'key': key,
            'value': value
        }
        collection.insert_one(dado)

def filtrarDados(rawJson):  # O JSON de resposta da API é extremamente grande, então filtramos para os dados mais recentes
    lista = []
    for timestamp in rawJson:
        lista.append(timestamp)
    lista = lista[140:]  # 140 dados mais recentes
    for n in lista:
        del rawJson[n]


def requestParaDB(link,indicador,nomeDoAtivo):
    r = requests.get(link)
    file = r.json()
    rawJson = file[indicador]
    filtrarDados(rawJson)
    if indicador == 'Time Series (Daily)':
        rawJson = tirarOPontinho(rawJson)
    print(rawJson)
    salvar_json_no_banco(nomeDoAtivo, indicador, rawJson)

#  A API gratuita da Alpha Vantage tem limite de 5 requisições por minutos
# ------------------------------------------------------------------------------------------------------------------------------------------
# PETR4 (Petrobrás)
# requestParaDB('https://www.alphavantage.co/query?function=SMA&symbol=PETR4.SA&interval=daily&time_period=20&series_type=close&apikey=08WB6TZXDDI5RM8S',
#               'Technical Analysis: SMA','PETR4.SA')
# requestParaDB('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=PETR4.SA&outputsize=full&apikey=23211',
#               'Time Series (Daily)','PETR4.SA')
# requestParaDB('https://www.alphavantage.co/query?function=RSI&symbol=PETR4.SA&interval=daily&time_period=20&series_type=close&apikey=23321',
#               'Technical Analysis: RSI','PETR4.SA')
#
# ------------------------------------------------------------------------------------------------------------------------------------------
# VALE3.SA (Vale)
# requestParaDB('https://www.alphavantage.co/query?function=SMA&symbol=VALE3.SA&interval=daily&time_period=20&series_type=close&apikey=08WB6TZXDDI5RM8S',
#               'Technical Analysis: SMA','VALE3.SA')
# requestParaDB('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VALE3.SA&outputsize=full&apikey=23211',
#               'Time Series (Daily)','VALE3.SA')
# requestParaDB('https://www.alphavantage.co/query?function=RSI&symbol=VALE3.SA&interval=daily&time_period=20&series_type=close&apikey=23321',
#               'Technical Analysis: RSI','VALE3.SA')
#
# ------------------------------------------------------------------------------------------------------------------------------------------
# IGTA3 (Iguatemi)
# requestParaDB('https://www.alphavantage.co/query?function=SMA&symbol=IGTA3.SA&interval=daily&time_period=20&series_type=close&apikey=08WB6TZXDDI5RM8S',
#               'Technical Analysis: SMA','IGTA3.SA')
# requestParaDB('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IGTA3.SA&outputsize=full&apikey=23211',
#               'Time Series (Daily)','IGTA3.SA')
# requestParaDB('https://www.alphavantage.co/query?function=RSI&symbol=IGTA3.SA&interval=daily&time_period=20&series_type=close&apikey=23321',
#               'Technical Analysis: RSI','IGTA3.SA')
#
# ------------------------------------------------------------------------------------------------------------------------------------------
# BBDC4 (Bradesco)
# requestParaDB('https://www.alphavantage.co/query?function=SMA&symbol=BBDC4.SA&interval=daily&time_period=20&series_type=close&apikey=08WB6TZXDDI5RM8S',
#               'Technical Analysis: SMA','BBDC4.SA')
# requestParaDB('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BBDC4.SA&outputsize=full&apikey=23211',
#               'Time Series (Daily)','BBDC4.SA')
# requestParaDB('https://www.alphavantage.co/query?function=RSI&symbol=BBDC4.SA&interval=daily&time_period=20&series_type=close&apikey=23321',
#               'Technical Analysis: RSI','BBDC4.SA')

print('OK')