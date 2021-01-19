#######################COPIA WORKSCOPES DA REDE ####################

from pathlib import Path
import os
import shutil
path = Path(r"R:\Corporativo\Plan_Manutencao\Planejamento Heavy\Workscope\Workscope 2018")
lista = []
listaxls = []
for top, dirs, files in os.walk(path):
    for xls in files:
        lista.append(os.path.join(top, xls))

for arq in lista:
    if arq.endswith("XLS"):
        listaxls.append(arq)
    if arq.endswith("xls"):
        listaxls.append(arq)
    if arq.endswith("XLSX"):
        listaxls.append(arq)
    if arq.endswith("xlsx"):
         listaxls.append(arq)

# print(*listaxls, sep="\n")
# print(len(listaxls))
#
# file2 = open(r"C:\Temp\workscope\{}.txt".format('workscope'), 'w', encoding='utf-8', errors='surrogateescape')
# for item in listaxls:
#     file2.writelines("%s\n" % item)
#
# file2.close()

newpath = Path(r"C:\Users\paulo.roberto\Documents\Copied 2018")
count = 0
for item in listaxls:
    shutil.copy(listaxls[count], newpath)
    count +=1