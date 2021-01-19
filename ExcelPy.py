# import os
# os.chdir(r"C:\Users\paulo.roberto\Documents\Python\Using Excel")
# import pandas as pd
# file = 'Mov_Estoque.xlsx'
# xl = pd.ExcelFile(file)
# df1 = xl.parse('FNDWRR')
# # print(df1)
#
# lista = [1, 4, 5, 12, 19, 21, 22, 33]
# print(list(lambda x: x%2 == 0, lista))
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in
#
# import os
# print(os.getcwd())
#
# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import matplotlib.pyplot as plt
# import seaborn as sns  # visualization tool
#
# # Input data files are available in the "../input/" directory.
# # For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
#
# from subprocess import check_output
# print(check_output(["ls", "../input"]).decode("utf8"))
#
# # Any results you write to the current directory are saved as output

# import os
# import shutil
# path = (r"R:\Corporativo\Plan_Manutencao\Planejamento Heavy\Workscope\Workscope 2019")
# diretorios = []
# idcount = 0
# pathws = []
# for diretorio in os.walk(path):
#     diretorios.append(diretorio)
#     if diretorios[idcount].
#         pathws.append(diretorios)
#     idcount += 1
#
#     #pasthws.append(str("R:\Corporativo\Plan_Manutencao\Planejamento Heavy\Workscope\Workscope 2019")+diretorio)
#
# print(pathws)
# print(diretorios[0])

import glob
# import os
# path = (r"C:\Temp\workscope")
# lista = []
# count = 0
# for file1 in os.walk(path):
#     for file2 in file1:
#         for file3 in file2:
#             if file3.endswith(".xls"):
#                 lista.append(file3)
#             if file3.endswith(".xlsx"):
#                 lista.append(file3)
#             if file3.endswith(".XLSX"):
#                 lista.append(file3)
#             if file3.endswith(".XLS"):
#                 lista.append(file3)
#
# print(*lista, sep="\n")
# print(len(lista))
#
# from pathlib import Path
# import os
# import shutil
# path = Path(r"R:\Corporativo\Plan_Manutencao\Planejamento Heavy\Workscope\Workscope 2019")
# lista = []
# listaxls = []
# for top, dirs, files in os.walk(path):
#     for xls in files:
#         lista.append(os.path.join(top, xls))
#
# for arq in lista:
#     if arq.endswith("XLS"):
#         listaxls.append(arq)
#     if arq.endswith("xls"):
#         listaxls.append(arq)
#     if arq.endswith("XLSX"):
#         listaxls.append(arq)
#     if arq.endswith("xlsx"):
#          listaxls.append(arq)

# print(*listaxls, sep="\n")
# print(len(listaxls))
#
# file2 = open(r"C:\Temp\workscope\{}.txt".format('workscope'), 'w', encoding='utf-8', errors='surrogateescape')
# for item in listaxls:
#     file2.writelines("%s\n" % item)
#
# file2.close()
#
# newpath = Path(r"C:\Users\paulo.roberto\Documents\Copied")
# count = 0
# for item in listaxls:
#     shutil.copy(listaxls[count], newpath)
#     count +=1
#

import openpyxl as op
import pandas as pd
from pathlib import Path
import os
os.chdir(r"C:\Users\paulo.roberto\Documents\Copied")
path = Path(r"R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Diretoria de Manutenção\Custo de Manutenção\ACTF-WO\2019\6.Junho\PR-AKB(01253)")
lista = []
for top, dirs, files in os.walk(path):
    for xls in files:
        if xls == 1 :
            lista.append(os.path.join(top, xls))

print(*lista, sep="\n")