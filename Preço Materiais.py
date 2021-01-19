import os
import pandas as pd

os.chdir(r'\\azul.corp\arquivos\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Indicadores-Analise\Movimento Estoque\Listagem PAC')

files = os.listdir()
big_frame = pd.DataFrame()
dicpn = {}
contbig = 0

for file in files:
    arq = pd.read_csv(file, quoting=3, delimiter=';',header=1, encoding='ANSI', thousands='.', decimal=',', low_memory=False, error_bad_lines=True, index_col=False)
    arq['Unitario'] = arq['Valor Final'] / arq['Qtd Final']
    arq['Origem'] = os.path.basename(file)
    big_frame = big_frame.append(arq, ignore_index=True,sort=False)

Listafinal = big_frame.to_excel("listafinal.xlsx")
# for item in big_frame['Item']:
#     dicpn.update ({big_frame['Item'].values[contbig]: [big_frame["Periodo"].values[contbig],
#                                                       big_frame["Descricao"].values[contbig],
#                                                       big_frame["Qtd Inicial"].values[contbig],
#                                                       big_frame["Qtd Entradas"].values[contbig],
#                                                       big_frame["Valor Entradas"].values[contbig],
#                                                       big_frame["Qtd Saidas"].values[contbig],
#                                                       big_frame["Valor Saidas"].values[contbig],
#                                                       big_frame["Qtd Final"].values[contbig],
#                                                       big_frame["Valor Final"].values[contbig],
#                                                       big_frame["Unitario"].values[contbig],
#                                                       big_frame["Origem"].values[contbig]]})
#     contbig +=1
#
# # print(big_frame.loc[big_frame['Item']=='MS24665-377'])
# print(dicpn['MS24665-377'])