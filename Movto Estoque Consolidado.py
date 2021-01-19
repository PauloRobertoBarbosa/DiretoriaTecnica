import pandas as pd
import os
os.chdir(r'C:\Users\paulo.roberto\Documents\Movto Estoque Consolidado')
movestoque = pd.read_excel('Movimento estoque consolidado - 2019.xlsx')
cols = list(movestoque.head(0))
movestoque['Acft'] = movestoque['Aplicacao'].str[-5:]
movestoque['Acft'] = movestoque['Acft'].str[:2]+'-'+movestoque['Acft'].str[-3:]

dicttran = {'transaction_id': [], 'WO': []}

countwo = 0

for i in movestoque.index:
    if str(movestoque['Transaction Reference'][i]).find('WO: ') != -1:
        dicttran['transaction_id'].append(movestoque['Transaction Id'][i])
        dicttran['WO'].append(movestoque['Transaction Reference'][i][41:47])

dfwo = pd.DataFrame(dicttran)
print(dfwo)