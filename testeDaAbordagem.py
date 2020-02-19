import matplotlib.pyplot as plt
from pymongo import MongoClient

x = []


fig1,ax1 = plt.subplots()
fig2,ax2 = plt.subplots()
fig3,ax3 = plt.subplots()
fig4,ax4 = plt.subplots()

def makeXandYList(json):
    global x
    y = []
    for i in x:
        y.append(json[i]['close'])
    return y

def carregar_jsons_do_banco(nome_do_ativo, indicador):
    dicJson = {}
    client = MongoClient()
    db = client.get_database('banco_de_dados')
    collection = db.get_collection('collect')

    lista_do_ativo = []

    for item in collection.find({'nome do ativo': nome_do_ativo, 'indicador': indicador}):
        key = item['key']
        value = item['value']
        item_limpo = {key: value}
        lista_do_ativo.append(item_limpo)

    for index in lista_do_ativo:
        for timestamp in index:
            dicJson[timestamp] = index[timestamp]

    return dicJson

valeJson = carregar_jsons_do_banco('VALE3.SA','Time Series (Daily)')

for time in valeJson:
    x.append(time)
x.reverse()

yVale = makeXandYList(valeJson)

petr4Json = carregar_jsons_do_banco('PETR4.SA','Time Series (Daily)')
yPetr4 = makeXandYList(petr4Json)

igta3Json = carregar_jsons_do_banco('IGTA3.SA','Time Series (Daily)')
yIgta3 = makeXandYList(igta3Json)

bbdc4Json = carregar_jsons_do_banco('BBDC4.SA','Time Series (Daily)')
yBbdc4 = makeXandYList(bbdc4Json)

ax1.plot(x,yVale)
ax1.set_title('VALE3.SA')
ax2.plot(x,yPetr4)
ax2.set_title('PETR4.SA')
ax3.plot(x,yIgta3)
ax3.set_title('IGTA3.SA')
ax4.plot(x,yBbdc4)
ax4.set_title('BBDC4.SA')

plt.xlabel('Date')
plt.ylabel('Closing Price')

fig1.autofmt_xdate()
fig2.autofmt_xdate()
fig3.autofmt_xdate()
fig4.autofmt_xdate()

plt.tight_layout()
plt.show()