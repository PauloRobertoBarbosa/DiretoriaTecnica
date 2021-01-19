import pandas as pd
import os

os.chdir(r'\\azul.corp\arquivos\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Realizado\Actual-2020\11.Nov-20')

df = pd.read_excel('11 2020 _ Relatório movimentação de entradas e saídas_com IPE.xlsx', sheet_name='Movto Estoque Classificado')

dfheavy = df[df["Reclassifica Ativo"]=='SIM']
dfheavyG = dfheavy.groupby(['acftWO', 'Fleet', 'CLASSIFICAÇÃO CONTÁBIL'])['ValorFinal'].sum()
for i in dfheavyG:
    if dfheavy['Fleet'] == 'A330':
        dfheavy['TipoFleet'] = 'A'

writer = pd.ExcelWriter('output.xlsx')

dfheavyG.to_excel(writer, merge_cells=False)
writer.save()

