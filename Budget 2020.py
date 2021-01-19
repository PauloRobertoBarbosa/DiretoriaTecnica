import openpyxl as xly
import os
os.chdir(r'C:\Users\paulo.roberto\Documents\Compilado PBI')
path = os.listdir()
fileopen = []
for i in path:
    if i.__contains__('~$'):
        pass
    else:
        value = i[0:4]
        plan = xly.load_workbook(i)
        ss_sheet = plan[value]
        ss_sheet.title = 'Budget2020'
        plan.save(i)
