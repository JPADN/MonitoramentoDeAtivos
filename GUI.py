from tkinter import *
from pymongo import MongoClient
import threading
import requests

class GUI:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Monitoramento de Ativos')
        self.ativo1 = 'VALE3.SA'
        self.ativo2 = 'PETR4.SA'
        self.ativo3 = 'IGTA3.SA'
        self.ativo4 = 'BBDC4.SA'

        self.width_da_listbox = 40
        self.height_da_listbox = 20

        self.t1 = Label(self.janela, text=self.ativo1)
        self.t1.grid(row=0, column=0)

        self.t2 = Label(self.janela, text=self.ativo2)
        self.t2.grid(row=0, column=1)

        self.t3 = Label(self.janela, text=self.ativo3)
        self.t3.grid(row=2, column=0)

        self.t4 = Label(self.janela, text=self.ativo4)
        self.t4.grid(row=2, column=1)

        # caixas de aviso compra/venda
        self.lb = Listbox(self.janela, width=self.width_da_listbox, height=self.height_da_listbox)
        self.lb.grid(row=1, column=0)

        self.lb2 = Listbox(self.janela, width=self.width_da_listbox, height=self.height_da_listbox)
        self.lb2.grid(row=1, column=1)

        self.lb3 = Listbox(self.janela, width=self.width_da_listbox, height=self.height_da_listbox)
        self.lb3.grid(row=3, column=0)

        self.lb4 = Listbox(self.janela, width=self.width_da_listbox, height=self.height_da_listbox)
        self.lb4.grid(row=3, column=1)

    # O nome deve ser igual ao das variáveis ativo1, ativo2...
    def ordem_de_compra(self,nome_do_ativo, tempo):
        d = {self.ativo1: self.lb, self.ativo2: self.lb2, self.ativo3: self.lb3, self.ativo4: self.lb4}
        d[nome_do_ativo].insert(END, 'COMPRA: ' + tempo)

    # O nome deve ser igual ao das variáveis ativo1, ativo2...
    def ordem_de_venda(self,nome_do_ativo, tempo):
        d = {self.ativo1: self.lb, self.ativo2: self.lb2, self.ativo3: self.lb3, self.ativo4: self.lb4}
        d[nome_do_ativo].insert(END, 'VENDA: ' + tempo)


