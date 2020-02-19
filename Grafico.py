import json
from pymongo import MongoClient

class Grafico:
    def __init__(self,axis,ativo,tela):
        self.ativo = ativo
        self.x = []
        self.ySma = [] # y da média móvel
        self.yClosing = [] # y do fechamento
        self.yRsi = [] # y do indice de força relativa
        self.rawJson = {} # rawJson armazena o json obtido pelo request do db
        self.rawJson2 = {}
        self.rawJson3 = {}
        self.pos = 0 # usado em ReqListVerif(), verifCruzamento(), verifRsi: é utilizado para obter a posição atual de algum indicador e verificar propriedades,
                     # no caso de ReqListVerif() é utilizado para limitar a quantidade de dados do gráfico a fim de n ficar muita informação
        self.timestampList = []
        self.index = 0 # usado em makeXandYList() para que possamos percores o json de forma sequencial até o seu fim
        self.plot = axis # é o atributo do gráfico do objeto, por isso passamos o axis do subplot como argumento no __init__ (assista matplotlib: subplots do corey schafer)
        self.tela = tela


    def carregar_jsons_do_banco(self,nome_do_ativo, indicador):
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


    def dbParaObjeto(self):
        self.rawJson = self.carregar_jsons_do_banco(self.ativo,'Technical Analysis: SMA')
        self.rawJson2 = self.carregar_jsons_do_banco(self.ativo,'Time Series (Daily)')
        self.rawJson3 = self.carregar_jsons_do_banco(self.ativo,'Technical Analysis: RSI')


    def makeXandYList(self):

        def filtrarData(string):
            string = string.split('-')
            return f'{string[1]}/{string[2]}'

        try:

            self.x.append(filtrarData(self.timestampList[self.index]))

            self.ySma.append(float(self.rawJson[self.timestampList[self.index]]['SMA']))
            self.yClosing.append(float(self.rawJson2[self.timestampList[self.index]]['close']))
            self.yRsi.append(float(self.rawJson3[self.timestampList[self.index]]['RSI']))

            self.index += 1

        except IndexError:
            self.index = 0

        print(self.ativo)
        print(f'x = {self.x}')
        print(f'ySma = {self.ySma}')
        print(f'yClosing = {self.yClosing}')
        print(f'yRsi = {self.yRsi}')
        print()


    def ReqListVerif(self):

        self.makeXandYList()
        if self.pos > 0:
            self.verifCruzamento()
            # self.verifRsi()

            if self.pos > 6:
                del self.x[0]
                del self.ySma[0]
                del self.yClosing[0]
                del self.yRsi[0]
            else:
                self.pos += 1
        else:
            self.pos += 1

    def demonstrar(self):
        self.dbParaObjeto()

        for timestamp in self.rawJson:
            self.timestampList.append(timestamp)
        self.timestampList.reverse()


    def verifCruzamento(self):
        try:
            if (self.yClosing[self.pos] > self.ySma[self.pos]) and (self.yClosing[self.pos - 1] < self.ySma[self.pos - 1]):
                print(f'COMPRE! Cruzamento em {self.x[self.pos]}')
                self.tela.ordem_de_compra(self.ativo,f'Cruzamento em {self.x[self.pos]}')
            elif (self.yClosing[self.pos] < self.ySma[self.pos]) and (self.yClosing[self.pos - 1] > self.ySma[self.pos - 1]):
                print(f'VENDA! Cruzamento em {self.x[self.pos]}')
                self.tela.ordem_de_venda(self.ativo,f'Cruzamento em {self.x[self.pos]}')

        except IndexError:
            print('IndexError')
            print(f'Pos = {self.pos}, lenSma = {len(self.ySma)}, lenClo = {len(self.yClosing)}')

    # def verifRsi(self):
    #     if self.yRsi[self.pos] > 69:
    #         print(f'VENDA! RSI Alto em {self.x[self.pos]}')
    #         self.tela.ordem_de_venda(self.ativo, f'RSI Alto em {self.x[self.pos]}')
    #
    #     elif self.yRsi[self.pos] < 31:
    #         print(f'COMPRE RSI Baixo em {self.x[self.pos]}')
    #         self.tela.ordem_de_compra(self.ativo,f'RSI Baixo em {self.x[self.pos]}')

