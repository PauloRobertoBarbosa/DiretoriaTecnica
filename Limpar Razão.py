import os

os.chdir(r'C:\Users\paulo.roberto\Documents\Razão VP Tec')
path = r'C:\Users\paulo.roberto\Documents\Razão VP Tec'
listrazao = []
listaok = []
listatratada = []
conta = 0

for arq in os.listdir(path):

    with open('{}'.format(arq),encoding='ANSI') as razao:
        razao = razao.readlines()
        for row in (razao):
            listrazao.append(row)

    for linha in razao:
        contagem = linha.count(';')

        if contagem == 78:
            listaok.append(linha)

    for linha in listrazao:
        contagem = linha.count(';')
        if contagem < 78:
            if listrazao[conta].count(';') + listrazao[conta+1].count(';') == 78:
                rowap1 = listrazao[conta]+listrazao[conta+1]
                listatratada.append(rowap1)
            if listrazao[conta].count(';') + listrazao[conta+1].count(';') + listrazao[conta+2].count(';') == 78:
                rowap2 = listrazao[conta] + listrazao[conta + 1]+ listrazao[conta + 2]
                listatratada.append(rowap2)
            conta += 1

listafim = listaok + listatratada

with open('newfile.txt', 'w') as Razao:
    for newrow in listafim:
        Razao.writelines(newrow)

Razao.close()