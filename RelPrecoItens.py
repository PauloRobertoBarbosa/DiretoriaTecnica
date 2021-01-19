import pandas as pd
import os

os.chdir(r'R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Indicadores-Analise\Movimento Estoque\Listagem PAC')

dflistagem = pd.DataFrame(columns=['Periodo','Item','Descricao','Qtd Inicial','Valor Inicial','Qtd Entradas','Valor Entradas','Qtd Saidas','Valor Saidas','Qtd Final','Valor Final'])

for file in os.listdir():
   df =  pd.read_csv(file, quoting=3, delimiter=';', skiprows=2, encoding='ANSI', thousands='.', decimal=',', low_memory=False, error_bad_lines=True)
   dflistagem = dflistagem.append(df)

excel = pd.ExcelWriter(r'C:\Users\paulo.roberto\Documents\ResumoCASK\listagempac.xlsx',engine='xlsxwriter')

dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='JAN', value='01-01')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='FEV', value='01-02')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='MAR', value='01-03')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='ABR', value='01-04')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='MAI', value='01-05')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='JUN', value='01-06')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='JUL', value='01-07')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='AGO', value='01-08')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='SET', value='01-09')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='OUT', value='01-10')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='NOV', value='01-11')
dflistagem['Periodo'] = dflistagem['Periodo'].replace(regex='DEZ', value='01-12')

dflistagem['Médio']  = dflistagem['Valor Final'] / dflistagem['Qtd Final']
dflistagem['Periodo'] = pd.to_datetime(dflistagem['Periodo'], format='%d-%m-%y').dt.strftime('%d/%m/%Y')

dflistagem.to_excel(excel, sheet_name='Base')

excel.save()
#

#
# pac = pd.read_excel(r'C:\Users\paulo.roberto\Documents\Teste preço itens.xlsx').fillna(0)
#
# # .set_index(['PN'], inplace=True)
# # dicpn = {}
# # contpac = 0
# #
# # for pn in pac:
# #     dicpn.update({pac['PN'].values[contpac]:[pac["CUSTO_PAC_ITEM"].values[contpac], pac["PRECO_UNITARIO_ITEM"].values[contpac], pac["PRECO_ULTIMA_COMPRA"].values[contpac]]})
# #     contpac +=1
# #
# #
# print(pac)
