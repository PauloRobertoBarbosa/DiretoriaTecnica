import pandas as pd
from fuzzywuzzy import fuzz
import os

path = pd.read_excel(r'R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Indicadores-Analise\Movimento Estoque\Suporte classificação.xlsx')
suporte = pd.DataFrame(path)

listaclassificar = suporte['DESCRIPTION'].loc[suporte["Maintenance"] == 'Classificar']
listaclassificar2 = suporte['DESCRIPTION'].loc[suporte["Maintenance"] != 'Classificar']

# print(len(listaclassificar2))
classificacao = {}
listadesc = []
cont = 0
for x in suporte["DESCRIPTION"]:
    if suporte["Maintenance"][cont] == "Classificar":
        print(x)
        cont += 1

#         classificacao.update({suporte['DESCRIPTION'].values[cont]: [suporte['CLASS ORACLE'].values[cont]]})
#     cont += 1
#     # listadesc.append(x)

print(len(classificacao))
#
# path2 = pd.read_excel(r'C:\Users\paulo.roberto\Documents\Classificar Maintenance.xlsx')
# classificar = pd.DataFrame(path2)
# cont2 = 0
#
# classificacao2 = {}
# listadesc2 = []
# for item in classificar["WO_DESCRIPTION"]:
#     listadesc2.append(item)
#
# for x in listadesc:
#     for y in listadesc2:
#         if fuzz.ratio(x,y)>= 95:
#             print('The Ratio between {} and {} is :'.format(x, y), fuzz.ratio(x,y))
#         cont +=1

# print(classificar["WO_DESCRIPTION"][2])