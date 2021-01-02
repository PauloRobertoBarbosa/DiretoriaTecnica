import pandas as pd
import os

os.chdir(r'C:\Users\paulo.roberto\Documents\Movto Estoque Consolidado')

MovtoEstoque = pd.read_excel('Movimento estoque consolidado - 2019.xlsx')
print(MovtoEstoque.head(0))