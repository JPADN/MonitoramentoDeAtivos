# MonitoramentoDeAtivos
Projeto Final da disciplina INE5404

## O que é isto?

Uma aplicação que simula a análise técnica de ativos da bolsa de valores.

É feita uma análise técnica simples, onde quando há o cruzamento de uma Simple Moving Average(Média Móvel Simples) com o 
Closing (Preço de Fechamento) é imitido um sinal de compra ou venda, dependendo de quem está ultrapassando quem (SMA ou
Closing).

Simple Moving Average e Closing são os chamados indicadores técnicos, utilizados na análise técnica de ativos.

**Importante: esta não é uma aplicação fiel à análise técnica no trading, é uma aplicação que visa desenvolver conceitos de 
programação
com Python e orientação à objetos em cima de um contexto de trading, apenas.**

## Como funciona

São feitas requisições HTTP à API da [Alpha Vantage](https://www.alphavantage.co/), logo após filtra-se os dados e 
armazena-os em *MongoDB*.

Estes dados são pares chave-valor nos quais a chave é uma timestamp e o valor é o valor do indicador técnico no momento 
da timestamp.

Ao executar o arquivo main.py, será requisitado ao banco de dados as informações de cada indicador técnico, e então será 
simulado o monitoramento dos indicadores técnicos dos ativos:

### Simulação

Será percorrido um array X com as timestamps juntamento com um array y com os valores dos indicadores, desde uma data definida
dentro do código até o dado mais recente, e quando o Closing cruzar o SMA na subida temos um sinal de compra, caso ocorra o 
contrário, temos um sinal de venda.

## Executar

### 1º Passo: Prover input ao banco de dados

É necessário que você tenha um banco de dados MongoDB local rodando na porta localhost:27017.

Execute dbInput.py:

Será criado um database com o nome "banco_de_dados" e uma collection com o nome "collect".

Será possível rodar apenas 5 vezes a função requestParaDB por minuto, haja vista o limite de requests que a API possui.

### 2º Passo: Execute o arquivo main.py

Este arquivo irá instanciar uma janela do Tkinter que será responável por mostrar os avisos de compra e venda.

Será instanciado também uma janela do Matplotlib que irá plotar 4 gráficos (um para cada ativo), onde em cada gráfico 
haverão 2 métricas, a SMA (Simple Moving Average) e a RSI (Relative Strength Indicator).

