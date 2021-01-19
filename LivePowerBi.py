import pandas as pd
import os

os.chdir(r'C:\Users\paulo.roberto\Downloads\Mestre Power bi\Live 30-04')

dados = pd.read_excel('Vendas.xlsx', parse_dates=['DataEmissao'])
dados2 = dados.groupby(['DataEmissao', 'cdProduto'], as_index=False)['ValorVenda'].sum()
print(dados2.head())
