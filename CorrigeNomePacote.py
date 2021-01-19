import os
import pandas as pd
# status = pd.ExcelFile(r"R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Indicadores-Analise\Movimento Estoque\Status de Aeronaves em Check.xlsx")
status = pd.ExcelFile(r"R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Diretoria de Manutenção\Custo de Manutenção\ACTF-WO\Consolidado - Apurações\Checks realizados.xlsx")
statusacft = status.parse()
# print(statusacft.head(0))
# Consolidado = statusacft.parse()
# statusacft = status['Consolidado'].parse()

listapacotes = []
for itempacote in statusacft["Check"]:
    itempacote.strip()
    listapacotes.append(itempacote)

listacheck = []

for i in listapacotes:
    listaitem = []
    listaitem = i.split('+')
    for check in listaitem:
        if check.strip() in listacheck:
            pass
        else:
            listacheck.append(check.strip())

listacheckfinal = []

for x in listacheck:
    listaitemcheck = []
    listaitemcheck = x.split('+')
    for checkfinal in listaitemcheck:
        if checkfinal.strip() in listacheckfinal:
            pass
        if checkfinal.__contains__(' – REDELIVERY'):
            pass
        else:
            listacheckfinal.append(checkfinal.strip())



print(*listacheckfinal, sep="\n")