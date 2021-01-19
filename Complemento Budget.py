import os
import pandas as pd
import openpyxl

os.chdir(r"C:\Users\paulo.roberto\Documents\Budget 2020 - complemento")

count = 0

for i in os.listdir():
    arquivo = pd.ExcelFile(i)
    ss=openpyxl.load_workbook(arquivo)
    for a in ss.sheetnames:
        ss_sheet = ss[a]
        ss_sheet.title = 'Budget'
        # print("New{}".format(i))
        ss.save("new{}".format(i))
    # ss_sheet = ss['Sheet']
    # ss_sheet.title = 'Budget'
    # ss.save(arquivo)
