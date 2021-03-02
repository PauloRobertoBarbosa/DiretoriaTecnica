import pandas as pd
import os

os.chdir(r'C:/Users/paulo.roberto/Documents/Base Razao')

razao = pd.read_csv('Realizado 2021.txt', quoting=3, delimiter=';', skiprows=0, encoding='ANSI', thousands='.', decimal=',', low_memory=False, error_bad_lines=True)
df = razao[['Filial','Descrição Filial','Centro de Custo','Descrição Centro de Custo','Conta','Descrição Conta','Tipo de Servico','Descrição Tipo de Servico','Prefixo da Aeronave','Descrição Prefixo da Aeronave','Líquido','Mês','Data GL','Origem','Categoria','Histórico','Fornecedor','Numero NF RI/AP','Data NF RI/AP','Detalhe Historico RI/AP','Criador RI/AP','Comentarios da PO','Observacoes da Aprovacao PO','Conta Contrapartida']]
plancont = pd.read_excel(r'//azul.corp/arquivos/Corporativo/Diretoria Tecnica/1-Gestão de Custos/Indicadores-Analise/Análise Mensal Realizado/Base_Dados 2019/Plano de Contas - Contas Resultado.xlsx')
#
plancont.rename(columns={'Valor':'Conta'}, inplace=True)

df = df.merge(plancont, how='left')
# df2340 = df[df['Centro de Custo']==2340]
# print(df2340.shape)
#
df['Mês'] = df['Mês'].replace(regex='JAN', value='01')
df['Mês'] = df['Mês'].replace(regex='FEV', value='02')
df['Mês'] = df['Mês'].replace(regex='MAR', value='03')
df['Mês'] = df['Mês'].replace(regex='ABR', value='04')
df['Mês'] = df['Mês'].replace(regex='MAI', value='05')
df['Mês'] = df['Mês'].replace(regex='JUN', value='06')
df['Mês'] = df['Mês'].replace(regex='JUL', value='07')
df['Mês'] = df['Mês'].replace(regex='AGO', value='08')
df['Mês'] = df['Mês'].replace(regex='SET', value='09')
df['Mês'] = df['Mês'].replace(regex='OUT', value='10')
df['Mês'] = df['Mês'].replace(regex='NOV', value='11')
df['Mês'] = df['Mês'].replace(regex='DEZ', value='12')

df['mes'] = df['Mês'].str[:2].astype(int)
df['ano'] = df['Mês'].str[3:].astype(int)

dflastyear = df[df['ano']==max(df['ano'])]
dflastmonth = dflastyear[dflastyear['mes']==max(dflastyear['mes'])]

for CC in dflastmonth['Centro de Custo'].unique():
    excel = pd.ExcelWriter(r'C:/Users/paulo.roberto/Documents/Base Razao/razao - 2021 - CC - {}.xlsx'.format(CC),engine='xlsxwriter')

    dfcc = df[df['Centro de Custo']==int(CC)].groupby(['Centro de Custo', 'ano', 'mes'])[['Líquido']].sum().sort_values((['Centro de Custo', 'ano', 'mes']))
    dfcc.to_excel(excel, sheet_name='CC')
    wb = excel.book
    ws = excel.sheets['CC']
    money_fmt = wb.add_format({'num_format': '#,##0'})
    ws.set_column('D:D',12,money_fmt)

    dfccconta = df[df['Centro de Custo']==int(CC)].groupby(['TIPO','Centro de Custo', 'ano','Conta','Descrição Conta','mes'])[['Líquido']].sum().sort_values((['TIPO','ano', 'mes','Conta']))
    dfccconta.to_excel(excel, sheet_name='CCConta')
    wb = excel.book
    ws = excel.sheets['CCConta']
    money_fmt = wb.add_format({'num_format': '#,##0'})
    ws.set_column('G:G',12,money_fmt)

    dfcccontaLastM = dflastmonth[dflastmonth['Centro de Custo']==int(CC)].groupby(['TIPO','Centro de Custo','Conta','Descrição Conta', 'Mês'])[['Líquido']].sum().sort_values((['TIPO','Conta','Mês']))
    dfcccontaLastM.to_excel(excel, sheet_name='LastMonth')
    wb = excel.book
    ws = excel.sheets['LastMonth']
    money_fmt = wb.add_format({'num_format': '#,##0'})
    ws.set_column('F:F',12,money_fmt)

    dfbase = df[df['Centro de Custo']==int(CC)]
    dfbase.to_excel(excel, sheet_name='Base', index=False)

    excel.save()