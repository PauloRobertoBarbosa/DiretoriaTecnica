import pandas as pd
import os

os.chdir(r'C:\Users\paulo.roberto\Documents\Movto Estoque Consolidado')

movestoque = pd.read_excel('Movimento estoque consolidado - 2019.xlsx')
cols = list(movestoque.head(0))
for i in cols:
    print(i)


