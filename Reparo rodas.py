import os
import pandas as pd

os.chdir(r"\\azul.corp\arquivos\Corporativo\Diretoria Tecnica\1-Gestão de Custos\IATA\2020")

arquivo = pd.ExcelFile("Reparo de Rodas e Freios - AV - 2019.xlsx")

df = pd.DataFrame()

sheets = list(arquivo.sheet_names)

count = 0

for i in sheets:
    dfsheets = pd.read_excel(arquivo, sheet_name = sheets[count], skiprows=1)
    df = df.append(dfsheets)
    count += 1

excel = pd.ExcelWriter(r'C:\Users\paulo.roberto\Documents\reparorodasefreios-AV.xlsx' ,engine='xlsxwriter')
df.to_excel(excel, sheet_name='rodasefreios - AV')

excel.save()