import shutil
import os
import sys

os.chdir(r'C:\Users\paulo.roberto\Documents')
files = os.listdir()
filedesttxt = r'C:\Users\paulo.roberto\Documents\Arquivos TXT'
filedestpdf = r'C:\Users\paulo.roberto\Documents\Arquivos PDF'
filedestpbi = r'C:\Users\paulo.roberto\Documents\Arquivos PBI'
filedestxls = r'C:\Users\paulo.roberto\Documents\Arquivos XLS'
filedestdoc = r'C:\Users\paulo.roberto\Documents\Arquivos Doc'
filedestppt = r'C:\Users\paulo.roberto\Documents\Arquivos PPT'

# #TEXT FILE
# for file in files:
#     if file.lower().__contains__(".txt"):
#         if os.path.isfile(file):
#             shutil.move(file, filedesttxt)
#
# #POWER BI FILE
# for file in files:
#     if file.lower().__contains__(".pbi"):
#         if os.path.isfile(file):
#             shutil.move(file, filedestpbi)
#
# #PDF FILE
# for file in files:
#     if file.lower().__contains__(".pdf"):
#         if os.path.isfile(file):
#             shutil.move(file, filedestpdf)
#
# #EXCEL FILE
# for file in files:
#     if file.lower().__contains__(".xls"):
#         if os.path.isfile(file):
#             shutil.move(file, filedestxls)
#
# #EXCEL FILE
# for file in files:
#     if file.lower().__contains__(".xlsx"):
#         if os.path.isfile(file):
#             shutil.move(file, filedestxls)
# #EXCEL FILE
# for file in files:
#     if file.lower().__contains__(".csv"):
#         if os.path.isfile(file):
#             shutil.move(file, filedestxls)
#
# #DOC FILE
# for file in files:
#     if file.lower().__contains__(".doc"):
#         if os.path.isfile(file):
#             shutil.move(file, filedestdoc)
#
# #POWER POINT FILE
# for file in files:
#     if file.lower().__contains__(".ppt"):
#         if os.path.isfile(file):
#             shutil.move(file, filedestppt)

listaextencao = ['txt','pbi','csv','xls','doc','ppt','pdf']

extencao = input('informe o tipo de arquivo que deseja mover: ')

def funextencao(extencao):
    if not extencao.lower() in listaextencao:
        print('Extenção não pode ser utilizada')
        sys.exit()
    else:
        dest = 'filedest{}'.format(extencao)
        for file in files:
            if file.lower().__contains__('.'+extencao):
                print(dest)
                print(file)

        #         shutil.move(file, dest)

funextencao(extencao)

# for tipo in listaextencao:

# print('filedest{}'.format(extencao))
