# import os
# import pandas as pd
#
# os.chdir(r'C:\Users\paulo.roberto\Documents\Arquivos XLS\Análise HE')
# df = pd.read_excel('Relatorio preço itens.xlsx', sheet_name='BASE')
# for i in df['CC'].unique():
#     excel = pd.ExcelWriter(r'RelatorioHE-{}.xlsx'.format(i),engine='xlsxwriter')
#     dfcc = df[df['CC'] == i]
#     dfcc.to_excel(excel, sheet_name=str(i), index=False)
#     excel.save()

# import os
# import pandas as pd

# os.chdir(r'C:\Users\paulo.roberto\Documents\Arquivos XLS\ContasCC')
# df = pd.read_excel('Principais Contas VP Tec.xlsx', sheet_name='Principais contas')
# for i in df['CC'].unique():
#     excel = pd.ExcelWriter(r'RelatorioPrincipaisContas-{}.xlsx'.format(i), engine='xlsxwriter')
#     dfcc = df[df['CC'] == i]
#     dfcc.to_excel(excel, sheet_name=str(i), index=False)
#     excel.save()


# import os
# import pandas as pd
# os.chdir(r'C:\Users\paulo.roberto\Documents\Arquivos TXT\Análise CAPEX')
#
# df = pd.DataFrame()
#
# for i in os.listdir():
#     dfi = pd.read_csv(i, quoting=3, delimiter=';', skiprows=26, encoding='ANSI', thousands='.', decimal=',', low_memory=False, error_bad_lines=True)
#     df = df.append(dfi)
#
# excel = pd.ExcelWriter(r'analisecapex.xlsx', engine='xlsxwriter')
# df.to_excel(excel, sheet_name='CAPEX', index=False)
# excel.save()

import random
starts_x = list(range(0,1000))
i = random.shuffle(starts_x)

print(starts_x)