import os
import pandas as pd

file = pd.read_csv(r'C:\Users\paulo.roberto\Documents\Realizado 2019 VP tecnica.txt', skiprows=26, encoding='cp1252', skip_blank_lines=True, sep=';')
df = pd.DataFrame(file)
df["Origem"] = "Realizado"
row,col = df.shape

# def make_float(num):
#     num = num.encode('latin-1').replace(' ','').replace(',','.')
#     return float(num)
#
print(df[["Origem","Centro de Custo"]])