import os
import pandas as pd
from pyxlsb import open_workbook as open_xlsb
os.chdir(r'C:\Users\paulo.roberto\Downloads\Plan PNT')
path = (r'C:\Users\paulo.roberto\Downloads\Plan PNT')

df = pd.DataFrame()

for i in os.listdir(path):
    with open_xlsb(i).get_sheet('Plan PNT') as sheet:
        df1 = pd.DataFrame(sheet.v for v in sheet)
        df = df.append(df1)
        sheet.close()

df1.to_excel("teste.xlsx")
