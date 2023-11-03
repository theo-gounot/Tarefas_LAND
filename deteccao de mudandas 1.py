import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\tgoun\OneDrive\Área de Trabalho"
                r"\Laboratorio\series temporais\1a amostra - Cleiton\ts1.txt",
                names=['Values'])                 
eixo_x = np.arange(1,len(df)+1)
plt.plot(eixo_x,df.Values)
def metodo_1():
    #o problema nesse codigo eh comparar um ponto e nao uma sequencia de pontos
    #isso aumenta a possibilidade de "changepoints"
    x = int(input())
    for n in range(x,len(df.Values)):
        ult = df.Values[n-x:n]
        geral = df.Values[:n]
        mu = ult.mean()
        mg = geral.mean()
        stdg = geral.std()
        if (mu > mg +2*stdg or mu < mg -2*stdg):
            print(n)
#250
def metodo1_2():
    contador = 0
    for n in range(1,len(df.Values)):
        ponto_atual = df.Values[n]
        desvio_atual = abs(df.Values[n]-df.Values[n-1])
        desvio_padrão = df.Values[:n].std(ddof=1)
        if desvio_atual > 3* desvio_padrão and contador == 0:
            contador += 1 
            ponto_importante = ponto_atual
            print(ponto_importante)
        elif desvio_atual > 3* desvio_padrão and contador < 2:
            contador += 1
        elif desvio_atual > 3* desvio_padrão and contador == 2:
            print("%s é change point"%(ponto_importante))
        else:
            contador = 0

def metodo_2():
    x = int(input("tamanho da janela"))
    for n in range(x,len(df.Values)-x):
        seg1 = df.Values[n-x:n]
        seg2 = df.Values[n:n+x]
        med1 = seg1.mean()
        med2 = seg2.mean()
        if abs(med2-med1) > df.Values.std():
            print(n)
            
metodo_2()