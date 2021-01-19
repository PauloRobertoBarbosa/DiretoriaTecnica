#######################COPIA WORKSCOPES DA REDE ####################
import xlrd
import openpyxl as op
from pathlib import Path
import os

# os.chdir(r"C:\Users\paulo.roberto\Documents\Copied 2018")
path = Path(r"R:\Corporativo\Plan_Manutencao\Planejamento Heavy\Workscope\Workscope 2019")
# path = Path(r"C:\Users\paulo.roberto\Documents\Copied 2018")
lista = []
listaxls = []
lista2 = []
for top, dirs, files in os.walk(path):
    for xls in files:
        if xls.__contains__("~$")==False and xls.__contains__(".pdf")==False and xls.lower().__contains__("workscope") and xls.lower().__contains__("xls"):
            lista.append(os.path.join(top, xls))

listausar = list(range(0, len(lista)))
listautilizada = []
for sheetusar in listausar:
    sheetname = xlrd.open_workbook(lista[sheetusar])
    sheets = sheetname.sheet_names()
    sheets = xlrd.open_workbook(lista[sheetusar], encoding_override='cp1252').sheet_names()
    workscope = ''
    for sheet in sheets:
        if sheet.lower()=='workscope':
            workscope = sheet
            filez = xlrd.open_workbook(lista[sheetusar], encoding_override='cp1252')
            listautilizada.append(sheetusar)

    try:
        book = filez.sheet_by_name(workscope)
        col1 = []
        wo = []
        wofim = []
        ncol = 0
        while book.ncols > ncol:
            for val in book.col(ncol):
                if val.value != '':
                    col1.append(val.value)
            ncol +=1
        acft = col1[col1.index('TAIL NUMBER')+1]
        acftmodel = col1[col1.index('ACFT MODEL')+1]
        tipo = ''
        for t in col1:
            if str(t).__contains__("- MAJOR")==True:
                tipo = t
        checktype = col1[col1.index(str(tipo))+1]
        mro = col1[col1.index('MRO')+1]
        plantat = col1[col1.index('PLANNED TAT')+1]
        realtat = col1[col1.index('REAL TAT')+1]
        schstartdate = col1[col1.index('SCHEDULE START DATE') + 1]
        schcompletion = col1[col1.index('SCHEDULE COMPLETION') + 1]
        realcompletion = col1[col1.index('REAL COMPLETION DATE') + 1]

        for numwo in col1:
            if type(numwo)==float:
                if len(str(numwo))==8:
                    wo.append(numwo)
        for iwo in wo:
            if iwo in wofim:
                pass
            else:
                wofim.append(iwo)
        arquivo = r"C:\Users\paulo.roberto\Documents\worscopeconsolidado 2019.xlsx"
        planworkscope = op.load_workbook(arquivo)
        ws = planworkscope["woworkscope"]
        maiorrow= ws.max_row+1

        for valcel in wofim:
            ws['A{}'.format(maiorrow)] = acft
            ws['B{}'.format(maiorrow)] = acftmodel
            ws['C{}'.format(maiorrow)] = checktype
            ws['D{}'.format(maiorrow)] = mro
            ws['E{}'.format(maiorrow)] = plantat
            ws['F{}'.format(maiorrow)] = realtat
            ws['G{}'.format(maiorrow)] = valcel
            ws['H{}'.format(maiorrow)] = schstartdate
            ws['I{}'.format(maiorrow)] = schcompletion
            ws['J{}'.format(maiorrow)] = realcompletion
            ws['K{}'.format(maiorrow)] = lista[sheetusar]
            maiorrow += 1

        planworkscope.save(arquivo)

        # arquivosgerados = open(r"C:\Users\paulo.roberto\Documents\{}.txt".format('arquivosutilizados'), 'w')
        # for item in listautilizada:
        #     arquivosgerados.writelines("%s\n" % item)

    except:
        pass