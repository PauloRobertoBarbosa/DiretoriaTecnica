# import os
#
# os.chdir(r"c:\temp")
# #
# # # Am I in the correct directory?
# #print(os.getcwd())
# #
# #print(dir(os))
# #
# # # Print all the current file names
# for f in os.listdir():
#     # If .DS_Store file is created, ignore it
#     if f == '.DS_Store':
#         continue
#
#     file_name, file_ext = os.path.splitext(f)
#     print(file_name)
# #
#     # One way to do this
#     f_title, f_course, f_number = file_name.split('-')
#
#     # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))
#
#     # Need to remove whitespace
#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     # f_number = f_number.strip()
#
#     # Want to remove the number sign?
#     # f_number = f_number.strip()[1:]
#
#     # One thing I noticed about this output is that if it was sorted by filename
#     # then the 1 and 10 would be next to each other. How do we fix this? One way we can fix this is to pad
#     # the numbers. So instead of 1, we'll make it 01. If we had hundreds of files then this would maybe need to be 001.
#     # We can do this in Python with zfill
#     f_number = f_number.strip()[1:].zfill(2)
#
#     # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))
#
#     # You have the power to reformat in any way you see fit
#     print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))
#
#     new_name = '{}-{}{}'.format(file_num, file_title, file_ext)
#
#     os.rename(fn, new_name)
#
#
# # # print(len(os.listdir()))
# import win32com
#
# outlook = win32com.client.gencache.EnsureDispatch ("MAPI.outlook")
#
# accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts;
#
# print(accounts)
# #
# def emailleri_al(folder):
#     messages = folder.Items
#     a=len(messages)
#     if a>0:
#         for message2 in messages:
#              try:
#                 sender = message2.SenderEmailAddress
#                 if sender != "":
#                     print(sender, file=f)
#              except:
#                 print("Ben hatayım")
#                 print(account.DeliveryStore.DisplayName)
#                 pass
#
#              try:
#                 message2.Save
#                 message2.Close(0)
#              except:
#                  pass

# import os
# files = os.chdir(r"c:\temp")
# lista_arquivos = []
# arq = os.listdir()
# for item in arq:
#     if item.__contains__('xlsx'):
#         lista_arquivos.append(item)
#
# import pandas as pd
# import numpy as np
# # arr = np.linspace(0, 50, 75).reshape(15, 5)
# # print(arr[3:6, 0])
# arr = np.arange(0, 16)
# print(2 / arr)
# import matplotl/ib.pyplot as plt
# year = [1950, 1970, 1990, 2010]
# pop = [2.519, 3.692, 5.263, 6.972]
#
# plt.scatter(year, pop)
# plt.show()

# a = [1, 2, 3, 4]
# b = [3, 9, 2, 6]
# plt.scatter(a, b)
# plt.show()
# import os
# import xlrd as xl
# # import pandas as pd
# # import numpy  as np
# listadir = []
# for x in os.listdir(r"C:\Users\paulo.roberto\Documents\Generson\AIV\WORKSCOPE"):
#     if x.__contains__(".xls"):
#         listadir.append(x)
# num_elementos = 1
# arquivo = 0
#
# while (arquivo < num_elementos):
#     arqopen = (listadir[arquivo])
#     file = xl.open_workbook(r"C:\Users\paulo.roberto\Documents\Generson\AIV\WORKSCOPE\{}".format(arqopen))
#     first_sheet = file.sheet_by_index(0)
#     listawo = []
#     iniciolinha = 24
#     totallinhas = first_sheet.nrows
#     Conteudolinhas = ''
#     cont = 24
#     inicio = 0
#     acft = ''
#     for x in range(24):
#         col = 0
#         for y in range(first_sheet.ncols):
#             print(first_sheet.cell(x, col))

        #     if first_sheet.cell_value(x, col).__contains__("PR"):
        #         acft = first_sheet.cell_value(x, col)
        #         col += 1
        # print(acft)

        # x +=1



        # if first_sheet.row_values(inicio).__contains__("PR-"):
        #     print(first_sheet.row_values(inicio))
        # inicio += 1


    # while cont >= iniciolinha and cont < totallinhas:
    #     if first_sheet.cell_type(cont, 1) is not 2:
    #         pass
    #     else:
    #         listawo.append(first_sheet.cell_value(cont, 1))
    #     cont += 1

#     arquivo += 1
#
# print(listawo)
#
#
# i = 'NR-0001'
# print(i[0:2])


class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

# Define some students
john = Student("John", 12, "male", 6, {"math":3.3})
jane = Student("Jane", 12, "female", 6, {"math":3.5})

# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())