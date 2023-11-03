import os 
import datetime as dt

#diretorios
data = os.listdir(r"C:\Users\tgoun\OneDrive\Área de Trabalho\Laboratorio\limpeza_de_dados_cleiton\wptagent-control") #botar diretório 
ndt_data = data[0]
other_data = data[1]
wpt_data = data[2]

datas = []

def f1():

    #bota todas as datas numa lista
    for loop1 in data: #percorre os 3 diretorios que tenho tisponiveis
        files = os.listdir(r"C:\Users\tgoun\OneDrive\Área de Trabalho\Laboratorio\limpeza_de_dados_cleiton\wptagent-control\%s"%loop1)
        for loop2 in files: #percorre os arquivos de cada diretorio
            if "." in loop2: 
                tipo = loop2.split(".") #separa o tipo de arquivo do resto do nome : "arquivo.txt" -> arquivo txt
                if tipo[1] == "json": #separa arquivos .json
                    infos = tipo[0].split("_") #separa as informacoes no nome do arquivo
                    for loop3 in infos:
                            if loop3.isdigit() == True: #confere se ha somente digitos no elemento, cumprindo essa condicao -> timestamp
                                 datas.append(loop3)                    
    #print(datas,len(datas))
    
    #o bloco a seguir toma como argumento a data/numero de dias e ve quantos teste testes foram feitos

    dia = input("insira a data(YYYY-MM-DD) ou a quantidade de dias passados ")
    n_testes = 0

    if dia.isdigit() == True: #dias passados
        dia = int(dia) #tranforma o numero de dias que passaram str -> int
        hoje = dt.datetime.now().date() #registra o dia atual
        data_em_questao = hoje - dt.timedelta(days=dia) #ve qual dia era n dias atras
        data_em_questao_refinada = str(data_em_questao).split() #separa YYYY-MM-DD de HH-MM-SS...
        for n in datas: 
            try:
                x = dt.datetime.fromtimestamp(int(n)) #tranforma os timstamp em data
                x = str(x).split() 
                if x[0] == data_em_questao_refinada[0]: #compara a parte referente a  YYYY-MM-DD a data em questao
                    n_testes += 1            
            except OSError:
                 break
    else: #dada uma data especifica
         for n in datas:
            try:
                x = dt.datetime.fromtimestamp(int(n))
                x = str(x).split()
                if x[0] == dia[0]: #compara o input no formato YYYY-MM-DD a parte referente de cada timestamp convertido
                    n_testes += 1
            except OSError:
                 break
    print(n_testes)

f1()
