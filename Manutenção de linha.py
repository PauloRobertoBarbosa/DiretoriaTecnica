
import os
import pandas as pd

os.chdir(r"\\azul.corp\arquivos\Corporativo\Manutencao\Passagem de serviço\1 - NOITE (23h00 às 07h00)\PLANEJAMENTO DE PERNOITE\2020")
path = (r"\\azul.corp\arquivos\Corporativo\Manutencao\Passagem de serviço\1 - NOITE (23h00 às 07h00)\PLANEJAMENTO DE PERNOITE\2020")

listaarquivos = []

df = pd.DataFrame()

for path, subdirs, files in os.walk(path):
    for name in files:
        if str(name).lower().__contains__("xls"):
            listaarquivos.append(os.path.join(path, name))

dffim = pd.DataFrame()

listItem = []
listDOCUMENT = []
listDESCRIPTION = []
listSKILL = []
listPICKLIST = []
listPriority = []
listHHPLANNINGTechnical = []
listHHPLANNINGTime = []
listHHPLANNINGAmount = []
listHHACCOMPLISHEDTechnical = []
listHHACCOMPLISHEDTime = []
listHHACCOMPLISHEDAmount = []
listacft = []
listdate = []
listwo = []

for i in listaarquivos:
    # print(i[-27:len(i)-5])
    arquivo = pd.ExcelFile(i)
    sheets = arquivo.book.sheets()
    for sheet in sheets:
        if sheet.visibility == 0:
            if str(sheet.name).lower().__contains__("pr-") or str(sheet.name).lower().__contains__("ps-"):
                dfacdate = arquivo.parse(sheet.name,skiprows=0,nrows= 1)
                dfwo = arquivo.parse(sheet.name,skiprows=2,nrows= 1)
                dfwo = dfwo[["WORK ORDER"]]
                dfacdate = dfacdate[["AIRCRAFT","DATE"]]
                df = arquivo.parse(sheet.name,skiprows=7)
                df1 = arquivo.parse(sheet.name,skiprows=5, nrows=1)
                df2 = arquivo.parse(sheet.name, skiprows=6, nrows=1)
                dfcolumnname = pd.DataFrame(df1.iloc[0, :])
                dfcolumnname = dfcolumnname.fillna(method='ffill')
                dfcolumnname1 = pd.DataFrame(df2.iloc[0, :])
                dfcolumnname1 = dfcolumnname1.fillna(method='ffill')
                listcolname = list(dfcolumnname[0])
                listcolname1 = list(dfcolumnname1[0])
                listcolnamefinal = []
                count = 0
                for b in listcolname:
                    listcolnamefinal.append(str(str(listcolname[count])+"-_-"+str(listcolname1[count])))
                    count +=1
                df.columns = listcolnamefinal
                df = df[df['H x h PLANNING-_-Amount'].notnull()]
                df['SKILL-_-No'] = ""

                if df['Item-_-No'].empty:
                    pass
                else:
                    df['acft'] = dfacdate['AIRCRAFT']
                    df['acft'].fillna(method='ffill', inplace=True)
                    if df['acft'].empty:
                        pass
                    else:
                        df['date'] = dfacdate['DATE']
                        df['date'].fillna(method='ffill', inplace=True)
                        df['wo'] = dfwo['WORK ORDER']
                        df['wo'].fillna(method='ffill', inplace=True)

                df.drop(df.columns[[0, 1, 2, 3]], axis=1, inplace=True)
                cols = pd.Series(df.columns)
                for dup in cols[cols.duplicated()].unique():
                    cols[cols[cols == dup].index.values.tolist()] = [dup + '.' + str(i) if i != 0 else dup for i in
                                                                     range(sum(cols == dup))]
                df.columns = cols

                if df.empty:
                    pass
                else:

                    for col in df['Item-_-No']:
                        listItem.append(col)
                    for col in df['DOCUMENT-_-No']:
                        listDOCUMENT.append(col)
                    for col in df['DESCRIPTION-_-No']:
                        listDESCRIPTION.append(col)
                    for col in df['SKILL-_-No']:
                        listSKILL.append(col)
                    for col in df['PICKLIST-_-No']:
                        listPICKLIST.append(col)
                    for col in df['Priority-_-No']:
                        listPriority.append(col)
                    for col in df['H x h PLANNING-_-Technical']:
                        listHHPLANNINGTechnical.append(col)
                    for col in df['H x h PLANNING-_-Time']:
                        listHHPLANNINGTime.append(col)
                    for col in df['H x h PLANNING-_-Amount']:
                        listHHPLANNINGAmount.append(col)
                    for col in df['H x h ACCOMPLISHED-_-Technical']:
                        listHHACCOMPLISHEDTechnical.append(col)
                    for col in df['H x h ACCOMPLISHED-_-Time']:
                        listHHACCOMPLISHEDTime.append(col)
                    for col in df['H x h ACCOMPLISHED-_-Amount']:
                        listHHACCOMPLISHEDAmount.append(col)
                    for col in df['acft']:
                        listacft.append(col)
                    for col in df['date']:
                        listdate.append(col)
                    for col in df['wo']:
                        listwo.append(col)

#
listfim = list(zip(listItem,listDOCUMENT,listDESCRIPTION,listSKILL,listPICKLIST,listPriority,listHHPLANNINGTechnical,listHHPLANNINGTime,listHHPLANNINGAmount,listHHACCOMPLISHEDTechnical,listHHACCOMPLISHEDTime,listHHACCOMPLISHEDAmount,listacft,listdate,listwo))

print(len(listItem))
print(len(listDOCUMENT))
print(len(listDESCRIPTION))
print(len(listSKILL))
print(len(listPICKLIST))
print(len(listPriority))
print(len(listHHPLANNINGTechnical))
print(len(listHHPLANNINGTime))
print(len(listHHPLANNINGAmount))
print(len(listHHACCOMPLISHEDTechnical))
print(len(listHHACCOMPLISHEDTime))
print(len(listHHACCOMPLISHEDAmount))
print(len(listacft))
print(len(listdate))

# df4 = pd.DataFrame(list(zip(listItem,listDOCUMENT,listDESCRIPTION,listSKILL,listPICKLIST,listPriority,listHHPLANNINGTechnical,listHHPLANNINGTime,listHHPLANNINGAmount,listHHACCOMPLISHEDTechnical,listHHACCOMPLISHEDTime,listHHACCOMPLISHEDAmount,listacft,listdate)), columns=['listItem','listDOCUMENT','listDESCRIPTION','listSKILL','listPICKLIST','listPriority','listHHPLANNINGTechnical','listHHPLANNINGTime','listHHPLANNINGAmount','listHHACCOMPLISHEDTechnical','listHHACCOMPLISHEDTime','listHHACCOMPLISHEDAmount','listacft','listdate'])
df4 = pd.DataFrame(listfim, columns=['listItem','listDOCUMENT','listDESCRIPTION','listSKILL','listPICKLIST','listPriority','listHHPLANNINGTechnical','listHHPLANNINGTime','listHHPLANNINGAmount','listHHACCOMPLISHEDTechnical','listHHACCOMPLISHEDTime','listHHACCOMPLISHEDAmount','listacft','listdate','listwo'])

df4['listacft'] = df4['listacft'].fillna(method='ffill')
df4['listdate'] = df4['listdate'].fillna(method='ffill')
df4['listwo'] = df4['listwo'].fillna(method='ffill')

excel = pd.ExcelWriter(r'C:\Users\paulo.roberto\Documents\Manut Linha\{}.xlsx'.format(str(i[-27:len(i) - 5] + "-" + sheet.name).replace("(", "").replace(")", "").replace('"', '')),engine='xlsxwriter')
df4.to_excel(excel, sheet_name='{}'.format(sheet.name))
excel.save()