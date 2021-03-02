import os
import pandas as pd

os.chdir(r'C:/Users/paulo.roberto/Documents/Arquivos TXT')

path = r"R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Indicadores-Analise\Análise Mensal Realizado\Base Razão"
lista = []
for top, dirs, files in os.walk(path):
    for file in files:
        lista.append((os.path.join(top,file)))

dfall = pd.DataFrame()

for i in lista:
    razao = pd.read_csv(i, quoting=3, delimiter=';', skiprows=26, encoding='ANSI',
                        thousands='.', decimal=',', low_memory=False, error_bad_lines=True,)
    df  = razao[
        ['Filial', 'Descrição Filial', 'Centro de Custo', 'Descrição Centro de Custo', 'Conta', 'Descrição Conta',
         'Tipo de Servico', 'Descrição Tipo de Servico', 'Prefixo da Aeronave', 'Descrição Prefixo da Aeronave',
         'Líquido', 'Mês', 'Data GL', 'Origem', 'Categoria', 'Histórico', 'Fornecedor', 'Numero NF RI/AP',
         'Data NF RI/AP', 'Detalhe Historico RI/AP', 'Criador RI/AP', 'Comentarios da PO',
         'Observacoes da Aprovacao PO', 'Conta Contrapartida']]

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

    dfall = dfall.append(df, ignore_index=True)

#Export
dfall.to_csv("testerazao.txt", sep=";", encoding='ANSI')