import os
import shutil

#
# path = r'R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Diretoria de Manutenção\Custo de Manutenção\ACTF-WO\Apuração Custos\2020'
# dest = r'R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Indicadores-Analise\Movimento Estoque\WorkScope - Heavy Check'
# works = r'R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Indicadores-Analise\Movimento Estoque\WorkScope - Heavy Check'
#
# listaarquivos = []
#
# listawork = [file for root, dirs, file in os.walk(works)]
# print(listawork)

#
# for root,dirs, files in os.walk(path):
#     for file in files:
#         if file.__contains__("xls"):
#             if file.lower().__contains__("workscope"):
#                 if file.lower().__contains__("final"):
#                     listaarquivos.append(os.path.join(root,file))
#                     # print(os.path.join(root,file))
# for i in listaarquivos:
#     shutil.copy(i,dest)
