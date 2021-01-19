import os
import pandas as pd

os.chdir(r'C:\Users\paulo.roberto\Documents\Arquivos XLS')

df = pd.read_excel('Hierarquia MNT Linha.xlsx')

for Geren in df['Geren'].unique():
    excel = pd.ExcelWriter(r'C:/Users/paulo.roberto/Documents/Arquivos XLS/Hierarquia - gerencia-{}.xlsx'.format(Geren),engine='xlsxwriter')
    dfgeren = df[df['Geren']==Geren]
    # dfgeren['Gerer'] = dfgeren['Gerer']#.astype(str)
    dfgeren.fillna
    dfgeren.to_excel(excel, sheet_name='Hierarquia', index=False)
    excel.save()
    # print(dfgeren.head(1))
