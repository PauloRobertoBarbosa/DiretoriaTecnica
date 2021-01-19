# import numpy as np
# import pandas as pd
# Make the array `my_array`
# my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
#
# # Print `my_array`
# print(my_array)

# class User:
#     def __init__(self, name, birthday):
#         self.name = name
#         self.birthday = birthday
#         print('Hello my name is ', name, 'eu nasci em ', birthday)
#
# name = input('Informe o nome')
# birthday = input('informe a data de nascimento')
# user1 = User(name, birthday)
#
# print(user1)

# labels = ['a', 'b', 'c']
# minha_lista = [10, 20, 30]
# arr = np.array([10, 20, 30])
# d  ={'a':10, 'b':20, 'c': 30}
# # ser = pd.Series(d.items(), labels)
#
# df = pd.DataFrame(np.random.randn(5, 4),index= 'A B C D E'.split(),columns= 'W X Y Z'.split())
#
# df['NEW'] = df['W'] + df['Z']
#
# print(df)
#
# import matplotlib
#
# import os
# os.get

# import pandas as pd
# import numpy as np
# import os
# import fuzzywuzzy
# # os.chdir(r'R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Indicadores-Analise\Movimento Estoque')
#
# movtoestoque = pd.read_excel(r'C:\Users\paulo.roberto\Documents\AZL___PAC___Rel__Mov__Entradas_020819_FINAL.xlsx', sheet_name='PAC jul 2019', header=0)
#
# df = pd.DataFrame(movtoestoque)
# # df['Transaction Reference2'] = df['Transaction Reference'].extract("WO: *")
#
# print(df['Transaction Reference'][15000].str.extract("WO: "))

from win32com.client import Dispatch
import os

os.chdir(r"C:\Users\paulo.roberto\Documents\MarcaRH")
outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
root_folder = outlook.Folders.Item(9)
rh = root_folder.Folders['Marcações RH']
messages = rh.Items

for x in messages:
    attach = x.Attachments
    attachment_item = attach.Item(1)
    dataemail = x.SentOn.strftime("%d-%m-%y")
    attachment_item.SaveAsFile(r'C:\Users\paulo.roberto\Documents\MarcaRH\{}{}.txt'.format('marcacoesRH', dataemail)) #Saves attachment to location