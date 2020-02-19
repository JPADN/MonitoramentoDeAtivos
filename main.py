import sys
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


from Grafico import Grafico
from GUI import GUI


tela = GUI()
fig, axis = plt.subplots(nrows=2,ncols=2)

objAxis1 = Grafico(axis[0][0],'VALE3.SA',tela)
objAxis1.demonstrar()
objAxis2 = Grafico(axis[0][1],'PETR4.SA',tela)
objAxis2.demonstrar()
objAxis3 = Grafico(axis[1][0],'IGTA3.SA',tela)
objAxis3.demonstrar()
objAxis4 = Grafico(axis[1][1],'BBDC4.SA',tela)
objAxis4.demonstrar()



def plotAnimation(i):
    global objAxis1,objAxis2,objAxis3, objAxis4

    if objAxis1.index == 140:
        sys.exit('Leitura do JSON concluída')


    objAxis1.ReqListVerif()
    objAxis2.ReqListVerif()
    objAxis3.ReqListVerif()
    objAxis4.ReqListVerif()


    objAxis1.plot.cla()  # Clear Axis (não ficar mudando de cor cada vez q atualiza)
    objAxis2.plot.cla()
    objAxis3.plot.cla()
    objAxis4.plot.cla()

    objAxis1.plot.plot(objAxis1.x, objAxis1.ySma, label='SMA',color='blue')
    objAxis1.plot.plot(objAxis1.x, objAxis1.yClosing, label='Closing', color='red')
    objAxis1.plot.plot(objAxis1.x, objAxis1.yRsi, label='RSI', color= 'green')

    objAxis2.plot.plot(objAxis2.x, objAxis2.ySma, label='SMA',color='blue')
    objAxis2.plot.plot(objAxis2.x, objAxis2.yClosing, label='Closing', color='red')
    objAxis2.plot.plot(objAxis2.x, objAxis2.yRsi, label='RSI', color= 'green')

    objAxis3.plot.plot(objAxis3.x, objAxis3.ySma, label='SMA',color='blue')
    objAxis3.plot.plot(objAxis3.x, objAxis3.yClosing, label='Closing', color='red')
    objAxis3.plot.plot(objAxis3.x, objAxis3.yRsi, label='RSI', color= 'green')

    objAxis4.plot.plot(objAxis4.x, objAxis4.ySma, label='SMA',color='blue')
    objAxis4.plot.plot(objAxis4.x, objAxis4.yClosing, label='Closing', color='red')
    objAxis4.plot.plot(objAxis4.x, objAxis4.yRsi, label='RSI', color= 'green')


    objAxis1.plot.legend(loc='upper left')
    objAxis2.plot.legend(loc='upper left')
    objAxis3.plot.legend(loc='upper left')
    objAxis4.plot.legend(loc='upper left')


    objAxis1.plot.set_title('VALE3.SA')
    # objAxis1.plot.set_ylim([10, 90])

    objAxis2.plot.set_title('PETR4.SA')
    # objAxis2.plot.set_ylim([10, 90])

    objAxis3.plot.set_title('IGTA3.SA')
    # objAxis3.plot.set_ylim([10, 90])

    objAxis4.plot.set_title('BBDC4.SA')
    # objAxis4.plot.set_ylim([10, 90])
    plt.style.use('fivethirtyeight')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), plotAnimation, interval=100)  # Qual figura, qual função, intevalo de tempo em ms
plt.show()
tela.janela.mainloop()


