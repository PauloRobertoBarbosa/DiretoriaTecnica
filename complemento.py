import os
import xlrd
from xlutils.copy import copy
import xlwt

path = r"C:\Users\paulo.roberto\Documents\Budget 2020 - complemento"
targetdir = (path + "New_Files/") #where you want your new files

if not os.path.exists(targetdir): #makes your new directory
    os.makedirs(targetdir)

for root,dir,files in os.walk(path, topdown=False): #all the files you want to split
    xlsfiles=[f for f in files] #can add selection condition here

for f in xlsfiles:
    # wb = xlrd.open_workbook(os.path.join(root, f), on_demand=True)
    # for sheet in wb.sheets(): #cycles through each sheet in each workbook
    #     newwb = copy(wb) #makes a temp copy of that book
    #     newwb._Workbook__worksheets = [ worksheet for worksheet in newwb._Workbook__worksheets if worksheet.name == sheet.name ]
    #     #brute force, but strips away all other sheets apart from the sheet being looked at
    #     newwb.save(targetdir + f.strip(".xls") + sheet.name + ".xls")
    #     #saves each sheet as the original file name plus the sheet name