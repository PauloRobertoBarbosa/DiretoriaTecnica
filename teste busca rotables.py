import os
import pandas as pd

os.chdir(r"C:\Users\paulo.roberto\Documents\Maintenance Reserve - IATA\Fleet")
for i in os.listdir():
    arquivo = pd.ExcelFile("{}".format(i))
    sheets = list(arquivo.sheet_names)
    count = 0
    df3 = pd.DataFrame()
    listvalue = []
    listperiod = []
    listname = []
    listarq = []

    for i in sheets:
        df = pd.read_excel(arquivo, sheet_name=sheets[count])
        indexdf = int(df[df.iloc[:, 0] == "PERIOD"].index[0] - 1)
        df2 = pd.DataFrame()
        df2 = df[df.index >= indexdf].reset_index()
        df2['arq'] = i
        df2.iloc[0, 1] = ""
        listcolumns = []
        dfcolumnname = pd.DataFrame(df2.iloc[0, :])
        dfcolumnname = dfcolumnname.fillna(method='ffill')
        dfcolumnname2 = pd.DataFrame(df2.iloc[1, :])
        dfcolumnname2 = dfcolumnname2.fillna(method='ffill')
        dfcolumnname3 = pd.DataFrame()
        dfcolumnname3['COLUMN1'] = dfcolumnname[0]
        dfcolumnname3['COLUMN2'] = dfcolumnname2[1]
        dfcolumnname3['COLUMN3'] = dfcolumnname3[['COLUMN1', 'COLUMN2']].astype(str).apply('(-_-)'.join, 1)
        df2.columns = dfcolumnname3['COLUMN3']

        df2 = df2.iloc[3:]
        df2 = df2.reset_index()

        for z in df2.columns:
            if str(z).lower().__contains__("invoice"):
                for a in df2['{}'.format(z)]:
                    listvalue.append(a)
                for b in df2['(-_-)PERIOD']:
                    listperiod.append(b)
                    listname.append(z)
                    listarq.append(i)

        for y in df2.columns:
            if str(y).lower().__contains__("actual"):
                for a in df2['{}'.format(y)]:
                    listvalue.append(a)
                for b in df2['(-_-)PERIOD']:
                    listperiod.append(b)
                    listname.append(y)
                    listarq.append(i)

        count += 1


    df3 = pd.DataFrame(list(zip(listperiod, listvalue, listname, listarq)),
                       columns=['PERIOD', 'VALUE', 'DESC', 'ARQUIVO'])

excel = pd.ExcelWriter(r'C:\Users\paulo.roberto\Documents\Maintenance Reserve - IATA\Resmat - All.xlsx',engine='xlsxwriter')
df3.to_excel(excel, sheet_name='Consolidado')
excel.save()

