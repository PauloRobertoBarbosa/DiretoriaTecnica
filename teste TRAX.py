import pandas as pd
import cx_Oracle
dsn_tns = cx_Oracle.makedsn(r'ORAODSTB578B.azul.corp', '1521', service_name='TRAX_ODS')
conn = cx_Oracle.connect(user=r'userselect', password=r'userselect', dsn=dsn_tns)
fh = conn.cursor()
fh.execute("""SELECT  
'01'||'/'||TO_CHAR(FLIGHT_DATE, 'MM')||'/'||TO_CHAR(FLIGHT_DATE, 'YYYY') MES, 
CASE  
WHEN AM.AC_TYPE = 'PILATUS-12' THEN 'PILATUS' 
WHEN AM.AC_TYPE = 'ATR72' THEN 'ATR' 
WHEN AM.AC_TYPE = 'E190' THEN 'EJET' ELSE AM.AC_TYPE END AC_TYPE,
((SUM(AF.FLIGHT_HOURS)*60)+SUM(AF.FLIGHT_MINUTES))/60 FH 
FROM ODB.AC_ACTUAL_FLIGHTS AF INNER JOIN ODB.AC_MASTER AM ON AF.AC = AM.AC 
WHERE AF.FLIGHT_DATE>='01-JAN-2019' AND AF.FLIGHT_DATE<='31-DEC-2019' 
GROUP BY '01'||'/'||TO_CHAR(FLIGHT_DATE, 'MM')||'/'||TO_CHAR(FLIGHT_DATE, 'YYYY'), AM.AC_TYPE """)
dffh = pd.DataFrame(fh, columns=['MES', 'FLEET', 'FH'])
print(dffh)