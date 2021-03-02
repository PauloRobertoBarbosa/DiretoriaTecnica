import os
import pandas as pd
from datetime import timedelta
os.chdir(r'\\azul.corp\arquivos\Corporativo\Planejamento Financeiro\FP Planejamento\Azul Reports\MX\2021\Relatório Gerencial de Frota\Schedule Package\Programação Heavy Checks')

atr = pd.read_excel('Heavy Check eventos - Capex.xlsx', sheet_name='ATR')
atr = atr[atr['Duração'].notna()]
atr = atr[['ACFT (MSN)','Duração','Início','Término']]

a320 = pd.read_excel('Heavy Check eventos - Capex.xlsx', sheet_name='A320')
a320 = a320[a320['Duração'].notna()]
a320 = a320[['ACFT','Duração','Início','Término']]

a330 = pd.read_excel('Heavy Check eventos - Capex.xlsx', sheet_name='A330')
a330 = a330[a330['Duração'].notna()]
a330 = a330[['ACFT','Duração','Início','Término']]

e1 = pd.read_excel('Heavy Check eventos - Capex.xlsx', sheet_name='E1')
e1 = e1[e1['Duração'].notna()]
e1 = e1[['ACFT (MSN)','Duração','Início','Término']]

b737 = pd.read_excel('Heavy Check eventos - Capex.xlsx', sheet_name='B737')
b737 = b737[b737['Duração'].notna()]
b737 = b737[['ACFT (MSN)','Duração','Início','Término']]

listaacft = []
listainicio = []
countatr = 0
counte1 = 0
counta320 = 0
counta330 =  0
countb737 = 0

for i in atr['ACFT (MSN)']:
    inicioteste = atr['Início'].iloc[countatr]
    while inicioteste  <= atr['Término'].iloc[countatr]:
        listaacft.append(i)
        listainicio.append(inicioteste)
        inicioteste = inicioteste + timedelta(days=1)
    countatr += 1

for i in a320['ACFT']:
    inicioteste = a320['Início'].iloc[counta320]
    while inicioteste  <= a320['Término'].iloc[counta320]:
        listaacft.append(i)
        listainicio.append(inicioteste)
        inicioteste = inicioteste + timedelta(days=1)
    counta320 += 1

for i in a330['ACFT']:
    inicioteste = a330['Início'].iloc[counta330]
    while inicioteste  <= a330['Término'].iloc[counta330]:
        listaacft.append(i)
        listainicio.append(inicioteste)
        inicioteste = inicioteste + timedelta(days=1)
    counta330 += 1

for i in e1['ACFT (MSN)']:
    inicioteste = e1['Início'].iloc[counte1]
    while inicioteste  <= e1['Término'].iloc[counte1]:
        listaacft.append(i)
        listainicio.append(inicioteste)
        inicioteste = inicioteste + timedelta(days=1)
    counte1 += 1

for i in b737['ACFT (MSN)']:
    inicioteste = b737['Início'].iloc[countb737]
    while inicioteste  <= b737['Término'].iloc[countb737]:
        listaacft.append(i)
        listainicio.append(inicioteste)
        inicioteste = inicioteste + timedelta(days=1)
    countb737 += 1

listabugetr = pd.DataFrame(zip(listaacft,listainicio))
listabugetr.columns = ['ACFT', 'DATA']
listabugetr.to_excel('teste.xlsx', index=False)

