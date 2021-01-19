# import os
# import openpyxl as xl
import pandas as pd
#
# os.chdir(r'C:\Users\paulo.roberto\OneDrive - Azul Linhas Aéreas\Estudos Python\2330')
#
# file = pd.ExcelFile(r'20191029_Cálculo HC malha Novembro_certo - AD_V3_Média - Copia - Copia.xlsm')
# sheet = file.parse('dados')
# print(sheet.head())
#
df1 = pd.DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
print(df1)