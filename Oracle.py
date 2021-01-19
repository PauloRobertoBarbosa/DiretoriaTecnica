import cx_Oracle
import pandas as pd
import itertools as it

dsn_tns = cx_Oracle.makedsn('ORAODSTB578B.azul.corp', '1521', service_name='TRAX_ODS')
conn = cx_Oracle.connect(user=r'userselect', password='userselect', dsn=dsn_tns)
cur = conn.cursor()
df = pd.DataFrame(cur.execute('select PN, Category from odb.pn_master'), columns=['PN','CATEGORY'])

print(df)

# for result in cur:
#     print (result)
