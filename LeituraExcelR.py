import os
import pandas as pd

os.chdir(r'C:/Users/paulo.roberto/Documents')
arq = pd.read_excel('Cópia de TOOLS (NDT) A330neo_COMPRA1.xlsx')
listareference = []
for i in (arq['STATUS']):
    listareference.append(i)

listareftratada = []
for i in listareference:
    for a in i.split(','):
        print(a)