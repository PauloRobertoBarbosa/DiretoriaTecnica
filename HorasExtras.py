# # # import pandas as pd
# # import os
# # # os.chdir(r"R:\Corporativo\Diretoria Tecnica\1-Gestão de Custos\Indicadores-Analise\Análise Mensal Realizado\Base_Dados 2019")
# # #
# # # file = pd.read_csv("Horas Extras.TXT", encoding="ANSI", delimiter="\t",thousands='.', decimal=',', low_memory=False, error_bad_lines=True)
# # # print(file.values)
# #
# # os.chdir(r"C:\Users\paulo.roberto\Documents")
# # name = input('Enter file:')
# # handle = open(name)
# #
# # counts = dict()
# # for line in handle:
# #     words = line.split()
# #     for word in words:
# #         counts[word] = counts.get(word,0) + 1
# #
# #
# # bigcount = None
# # bigword = None
# # for word,count in counts.items():
# #     if bigcount is None or count > bigcount:
# #         bigword = word
# #         bigcount = count
# #
# # print(counts.items())
# import os
# import pandas as pd
# import cx_Oracle
#
# dsn_tns = cx_Oracle.makedsn(r'ORAODSTB578B.azul.corp', '1521', service_name='TRAX_ODS')
# conn = cx_Oracle.connect(user=r'userselect', password=r'userselect', dsn=dsn_tns)
#
# picklist = conn.cursor()
# requisition = conn.cursor()
#
# picklist.execute("""
# SELECT DISTINCT
# TO_CHAR(PICKLIST_HEADER.TASK_CARD) TASK_CARD,
# TO_CHAR(WO_TASK_CARD.TASK_CARD_DESCRIPTION) TASK_CARD_DESCRIPTION,
# TO_CHAR(WO_TASK_CARD.SCHEDULE_TASK_CARD) SCHEDULE_TASK_CARD,
# TO_CHAR(PICKLIST_HEADER.WO) WO,
# TO_CHAR(WO_TASK_CARD.CHAPTER)CHAPTER,
# TO_CHAR((SELECT DESCRIPTION FROM ODB.ATA_CHAPTER_SECTION_PARAGRAPH
#      WHERE ATA_CHAPTER_SECTION_PARAGRAPH.CHAPTER = WO_TASK_CARD.CHAPTER
#      AND ATA_CATEGORY = 'CHAPTER')) AS ATA_DESCRIPTION ,
# TO_CHAR(PICKLIST_DISTRIBUTION.PN)PN,
# TO_CHAR(PN_MASTER.PN_DESCRIPTION)PN_DESCRIPTION,
# TO_CHAR(PN_MASTER.CATEGORY)PN_CATEGORY,
# TO_CHAR(PN_MASTER.STOCK_UOM) UOM_PN_MASTER,
# TO_CHAR(PN_MASTER .CATEGORY)CATEGORY,
# TO_CHAR(PICKLIST_HEADER.PICKLIST)PICKLIST,
# TO_CHAR(PICKLIST_DISTRIBUTION.PICKLIST_LINE)PICKLIST_LINE,
# TO_CHAR(PICKLIST_HEADER.PRIORITY)PRIORITY,
# TO_CHAR(PICKLIST_HEADER.CREATED_DATE)CREATED_DATE,
# TO_CHAR(PICKLIST_DISTRIBUTION.QTY)QTY,
# TO_CHAR(PICKLIST_HEADER.ORIGINAL_LOCATION)ORIGINAL_LOCATION,
# TO_CHAR(PICKLIST_HEADER.LOCATION)LOCATION,
# TO_CHAR(PICKLIST_HEADER.AC)AC,
# TO_CHAR(PICKLIST_HEADER.STATUS)STATUS,
# TO_CHAR(CAST ( NOTE_PAD.NOTES_TEXT AS VARCHAR2 ( 100 ) )) NOTES_TEXT,
# TO_CHAR('') AS REQUISITION,
# TO_CHAR('') AS REQUISITION_DESCRIPTION,
# TO_CHAR('') AS AUTHORIZATION,
# TO_CHAR('') AS ASSIGN_TO,
# TO_CHAR('') AS REQUISITION_TYPE,
# TO_CHAR('') AS CRIACAO_RQ,
# TO_CHAR('') AS SUM_QTY_AVAILABLE,
# TO_CHAR('') AS ORDER_NUMBER,
# TO_CHAR('') AS PO_ORACLE,
# TO_CHAR('') AS DATA_ENTREGA_PO,
#  TO_CHAR( CASE WHEN (PICKLIST_HEADER.STATUS='OPEN' AND
#              PICKLIST_HEADER.LOCATION IN ('PLU-P1-H3','PLU-P2-H3','PLU-P3-H20','PLU-P4-H20','PLU-P5-H19'))
#   THEN 'DISPONIVEL'
#   ELSE
#     CASE WHEN (PICKLIST_HEADER.STATUS='OPEN' AND
#                PICKLIST_HEADER.LOCATION IN ('VCP','PLU','SSA','REC','SDU','CNF','POA','CGB'))
#     THEN 'PENDENTE ALMOX'
#     ELSE
#       CASE WHEN (PICKLIST_HEADER.STATUS='CLOSED' AND
#                  PICKLIST_HEADER.LOCATION IN ('PLU','PLU-P1-H3','PLU-P2-H3','PLU-P3-H20','PLU-P4-H20','PLU-P5-H19'))
#       THEN 'ATENDIDO'
#       ELSE
#         CASE WHEN PICKLIST_HEADER.STATUS='TRANSFER'
#         THEN 'TRANSFERENCIA'
#         ELSE
#           CASE WHEN PICKLIST_HEADER.STATUS='CANCEL'
#           THEN 'CANCELADO'
#           ELSE '-'
#           END
#         END
#       END
#     END
#   END) SITUACAO,
# TO_CHAR('PICKLIST') AS ORIGEM
#
# FROM
#                           ODB.PICKLIST_HEADER PICKLIST_HEADER  LEFT JOIN   ODB.WO_TASK_CARD WO_TASK_CARD ON PICKLIST_HEADER.WO = WO_TASK_CARD.WO AND PICKLIST_HEADER.TASK_CARD = WO_TASK_CARD.TASK_CARD
#                           INNER JOIN ODB.WO ON PICKLIST_HEADER.WO = WO.WO
#                           INNER JOIN ODB.PICKLIST_DISTRIBUTION PICKLIST_DISTRIBUTION ON PICKLIST_HEADER.PICKLIST = PICKLIST_DISTRIBUTION.PICKLIST
#                           INNER JOIN
# (SELECT DISTINCT
# PNALL.PN,
# PNALL.PN_DESCRIPTION,
# PNALL.CATEGORY,
# PNALL.PN_INTERCHANGEABLE,
# PNALL.STOCK_UOM
#
# FROM
# (SELECT DISTINCT PM.PN, PM.PN_DESCRIPTION, PM.CATEGORY, PI.PN_INTERCHANGEABLE, PM.STOCK_UOM FROM ODB.PN_MASTER PM INNER JOIN
#                                                              ODB.PN_INTERCHANGEABLE PI ON PM.PN = PI.PN
# UNION
#
# SELECT DISTINCT PI.PN_INTERCHANGEABLE, PM.PN_DESCRIPTION, PM.CATEGORY, PM.PN, PM.STOCK_UOM FROM ODB.PN_MASTER PM
# INNER JOIN ODB.PN_INTERCHANGEABLE PI ON PM.PN = PI.PN) PNALL) PN_MASTER ON PN_MASTER.PN = PICKLIST_DISTRIBUTION.PN
#
# LEFT JOIN ODB.NOTE_PAD NOTE_PAD ON NOTE_PAD.NOTES = PICKLIST_HEADER.NOTES
#
# WHERE
# PICKLIST_HEADER.CREATED_DATE>=SYSDATE-250
# AND PICKLIST_HEADER.PRIORITY IN ('CHECK','PLAN','WSP')
# AND PICKLIST_DISTRIBUTION.TRANSACTION = 'REQUIRE'
# --AND NOTE_PAD.NOTES  ( + ) = PICKLIST_HEADER.NOTES
# AND WO.WO_CATEGORY = 'HEAVY' AND TO_CHAR(PICKLIST_HEADER.AC) = 'PR-AQK'
# """)
#
# dfpicklist = pd.DataFrame(picklist, columns = ['TASK_CARD', 'TASK_CARD_DESCRIPTION', 'WO', 'CHAPTER', 'ATA_DESCRIPTION', 'PN', 'PN_DESCRIPTION', 'UOM_PN_MASTER', 'CATEGORY', 'PICKLIST',' PICKLIST_LINE', 'PRIORITY', 'CREATED_DATE', 'QTY', 'ORIGINAL_LOCATION', 'LOCATION', 'AC', 'STATUS', 'NOTES_TEXT', 'SITUACAO', 'REQUISITION', 'REQUISITION_DESCRIPTION', 'AUTHORIZATION', 'ASSIGN_TO', 'REQUISITION_TYPE', 'QTY_REQUIRE', 'REQUIRE_DATE', 'CRIACAO_RQ', 'STATUS_1', 'SUM_QTY_AVAILABLE', 'ORDER_NUMBER', 'PO_ORACLE', 'DATA_ENTREGA_PO', 'REQ_LINE_STATUS', 'ORIGEM'])
#
# conn.close()
#
# print(dfpicklist)

import os
import pandas as pd
import cx_Oracle

dsn_tns = cx_Oracle.makedsn(r'ORAODSTB578B.azul.corp', '1521', service_name='TRAX_ODS')
conn = cx_Oracle.connect(user=r'userselect', password=r'userselect', dsn=dsn_tns)

requiremat = conn.cursor()

requiremat.execute("""
SELECT REQ.*, PHASE.PHASE, PHASE.MILESTONE_DESCR, PHASE.FLOWDAY, PHASE.AREA, PHASE.SITE FROM 
(SELECT DISTINCT 
TO_CHAR(PICKLIST_HEADER.TASK_CARD) TASK_CARD,
TO_CHAR(WO_TASK_CARD.TASK_CARD_DESCRIPTION) TASK_CARD_DESCRIPTION,
TO_CHAR(WO_TASK_CARD.SCHEDULE_TASK_CARD) SCHEDULE_TASK_CARD,
TO_CHAR(PICKLIST_HEADER.WO) WO,
TO_CHAR(WO_TASK_CARD.CHAPTER)CHAPTER,
TO_CHAR((SELECT DESCRIPTION FROM ODB.ATA_CHAPTER_SECTION_PARAGRAPH
     WHERE ATA_CHAPTER_SECTION_PARAGRAPH.CHAPTER = WO_TASK_CARD.CHAPTER
     AND ATA_CATEGORY = 'CHAPTER')) AS ATA_DESCRIPTION ,
TO_CHAR(PICKLIST_DISTRIBUTION.PN)PN,
TO_CHAR(PN_MASTER.PN_DESCRIPTION)PN_DESCRIPTION,
TO_CHAR(PN_MASTER.CATEGORY)PN_CATEGORY,
TO_CHAR(PN_MASTER.STOCK_UOM) UOM_PN_MASTER,
TO_CHAR(PN_MASTER .CATEGORY)CATEGORY,
TO_CHAR(PICKLIST_HEADER.PICKLIST)PICKLIST,
TO_CHAR(PICKLIST_DISTRIBUTION.PICKLIST_LINE)PICKLIST_LINE, 
TO_CHAR(PICKLIST_HEADER.PRIORITY)PRIORITY,
TO_CHAR(PICKLIST_HEADER.CREATED_DATE)CREATED_DATE,
TO_CHAR('01/'||TO_CHAR(PICKLIST_HEADER.CREATED_DATE, 'MM')||'/'||TO_CHAR(PICKLIST_HEADER.CREATED_DATE, 'RRRR')) PERIOD,
TO_CHAR(PICKLIST_DISTRIBUTION.QTY)QTY,
TO_CHAR(PICKLIST_HEADER.ORIGINAL_LOCATION)ORIGINAL_LOCATION,
TO_CHAR(PICKLIST_HEADER.LOCATION)LOCATION,
TO_CHAR(PICKLIST_HEADER.AC)AC,
TO_CHAR(PICKLIST_HEADER.STATUS)STATUS,
TO_CHAR(CAST ( NOTE_PAD.NOTES_TEXT AS VARCHAR2 ( 100 ) )) NOTES_TEXT,  
TO_CHAR('') AS REQUISITION,
TO_CHAR('') AS REQUISITION_DESCRIPTION,
TO_CHAR('') AS AUTHORIZATION,
TO_CHAR('') AS ASSIGN_TO,
TO_CHAR('') AS REQUISITION_TYPE,
TO_CHAR('') AS CRIACAO_RQ,
TO_CHAR('') AS SUM_QTY_AVAILABLE,
TO_CHAR('') AS ORDER_NUMBER,
TO_CHAR('') AS PO_ORACLE,
TO_CHAR('') AS DATA_ENTREGA_PO,
 TO_CHAR( CASE WHEN (PICKLIST_HEADER.STATUS='OPEN' AND 
             PICKLIST_HEADER.LOCATION IN ('PLU-P1-H3','PLU-P2-H3','PLU-P3-H20','PLU-P4-H20','PLU-P5-H19')) 
  THEN 'DISPONIVEL' 
  ELSE  
    CASE WHEN (PICKLIST_HEADER.STATUS='OPEN' AND 
               PICKLIST_HEADER.LOCATION IN ('VCP','PLU','SSA','REC','SDU','CNF','POA','CGB')) 
    THEN 'PENDENTE ALMOX' 
    ELSE     
      CASE WHEN (PICKLIST_HEADER.STATUS='CLOSED' AND 
                 PICKLIST_HEADER.LOCATION IN ('PLU','PLU-P1-H3','PLU-P2-H3','PLU-P3-H20','PLU-P4-H20','PLU-P5-H19')) 
      THEN 'ATENDIDO' 
      ELSE 
        CASE WHEN PICKLIST_HEADER.STATUS='TRANSFER'
        THEN 'TRANSFERENCIA'
        ELSE
          CASE WHEN PICKLIST_HEADER.STATUS='CANCEL'
          THEN 'CANCELADO'
          ELSE '-'
          END
        END
      END 
    END 
  END) SITUACAO,
CASE
WHEN SUBSTR(WO_TASK_CARD.TASK_CARD,0,2) ='NR' THEN TO_CHAR(WO_TASK_CARD.SCHEDULE_TASK_CARD) ELSE TO_CHAR(PICKLIST_HEADER.TASK_CARD) 
END TASK_F,
TO_CHAR('PICKLIST') AS ORIGEM

FROM 
                          ODB.PICKLIST_HEADER PICKLIST_HEADER  LEFT JOIN   ODB.WO_TASK_CARD WO_TASK_CARD ON PICKLIST_HEADER.WO = WO_TASK_CARD.WO AND PICKLIST_HEADER.TASK_CARD = WO_TASK_CARD.TASK_CARD
                          INNER JOIN ODB.WO ON PICKLIST_HEADER.WO = WO.WO
                          INNER JOIN ODB.PICKLIST_DISTRIBUTION PICKLIST_DISTRIBUTION ON PICKLIST_HEADER.PICKLIST = PICKLIST_DISTRIBUTION.PICKLIST 
                          INNER JOIN 
(SELECT DISTINCT
PNALL.PN,
PNALL.PN_DESCRIPTION,
PNALL.CATEGORY,
PNALL.PN_INTERCHANGEABLE,
PNALL.STOCK_UOM

FROM
(SELECT DISTINCT PM.PN, PM.PN_DESCRIPTION, PM.CATEGORY, PI.PN_INTERCHANGEABLE, PM.STOCK_UOM FROM ODB.PN_MASTER PM INNER JOIN
                                                             ODB.PN_INTERCHANGEABLE PI ON PM.PN = PI.PN
UNION

SELECT DISTINCT PI.PN_INTERCHANGEABLE, PM.PN_DESCRIPTION, PM.CATEGORY, PM.PN, PM.STOCK_UOM FROM ODB.PN_MASTER PM 
INNER JOIN ODB.PN_INTERCHANGEABLE PI ON PM.PN = PI.PN) PNALL) PN_MASTER ON PN_MASTER.PN = PICKLIST_DISTRIBUTION.PN

LEFT JOIN ODB.NOTE_PAD NOTE_PAD ON NOTE_PAD.NOTES = PICKLIST_HEADER.NOTES

WHERE 
PICKLIST_HEADER.CREATED_DATE>=SYSDATE-250
AND PICKLIST_HEADER.PRIORITY IN ('CHECK','PLAN','WSP')
AND PICKLIST_DISTRIBUTION.TRANSACTION = 'REQUIRE'
AND WO.WO_CATEGORY = 'HEAVY' AND TO_CHAR(PICKLIST_HEADER.AC) = 'PR-AQK'

UNION

SELECT DISTINCT 
TO_CHAR(REQUISITION_HEADER.TASK_CARD)TASK_CARD,
TO_CHAR(WO_TASK_CARD.TASK_CARD_DESCRIPTION)TASK_CARD_DESCRIPTION,
TO_CHAR(WO_TASK_CARD.SCHEDULE_TASK_CARD) SCHEDULE_TASK_CARD,
TO_CHAR(REQUISITION_HEADER.WO)WO,
TO_CHAR('') AS CHAPTER,
TO_CHAR('') AS ATA_DESCRIPTION,
TO_CHAR(REQUISITION_DETAIL.PN)PN,
TO_CHAR(REQUISITION_DETAIL.PN_DESCRIPTION)PN_DESCRIPTION,
TO_CHAR(PN_MASTER.CATEGORY)PN_CATEGORY,
TO_CHAR('') AS UOM_PN_MASTER,
TO_CHAR('') AS CATEGORY,
TO_CHAR('') AS PICKLIST,
TO_CHAR('') AS PICKLIST_LINE,
TO_CHAR(REQUISITION_HEADER.PRIORITY)PRIORITY,
TO_CHAR(REQUISITION_DETAIL.REQUIRE_DATE)CREATED_DATE,
TO_CHAR('01/'||TO_CHAR(REQUISITION_DETAIL.REQUIRE_DATE, 'MM')||'/'||TO_CHAR(REQUISITION_DETAIL.REQUIRE_DATE, 'RRRR')) PERIOD,
TO_CHAR(REQUISITION_DETAIL.QTY_REQUIRE)QTY,
TO_CHAR('') AS ORIGINAL_LOCATION,
TO_CHAR(REQUISITION_DETAIL.LOCATION)LOCATION,
TO_CHAR(REQUISITION_HEADER.AC)AC,
TO_CHAR(REQUISITION_DETAIL.STATUS)STATUS,
TO_CHAR('') AS NOTES_TEXT,
TO_CHAR(REQUISITION_HEADER.REQUISITION)REQUISITION, 
TO_CHAR(REQUISITION_HEADER.REQUISITION_DESCRIPTION)REQUISITION_DESCRIPTION,
TO_CHAR(REQUISITION_HEADER.AUTHORIZATION)AUTHORIZATION,
TO_CHAR(REQUISITION_DETAIL.ASSIGN_TO)ASSIGN_TO,
TO_CHAR(CASE WHEN (REQUISITION_HEADER.REQUISTION_TYPE='RMAN') 
THEN 'REPAROS E GARANTIAS'
ELSE 
  CASE WHEN (REQUISITION_HEADER.REQUISTION_TYPE='PO') 
  THEN 'PO COMPRAS'
  ELSE REQUISITION_HEADER.REQUISTION_TYPE 
  END
END) REQUISITION_TYPE,
TO_CHAR(REQUISITION_DETAIL.CREATED_DATE) CRIACAO_RQ,
TO_CHAR((SELECT NVL(SUM ( PID.QTY_AVAILABLE ),0) SOMA
FROM ODB.PN_INVENTORY_DETAIL PID,
ODB.PN_INTERCHANGEABLE PIA,
ODB.PN_INTERCHANGEABLE PIB,
ODB.PN_MASTER PM
WHERE PID.PN = PIA.PN_INTERCHANGEABLE
AND PIA.PN = PM.PN
AND PM.PN = PIB.PN
AND PIB.PN_INTERCHANGEABLE = REQUISITION_DETAIL.PN)) SUM_QTY_AVAILABLE,
TO_CHAR(ORDER_DETAIL.ORDER_NUMBER)ORDER_NUMBER,
TO_CHAR(ORDER_HEADER.LEGACY_SYSTEM_ORDER_NUMBER) PO_ORACLE,
TO_CHAR(ORDER_DETAIL.DELIVERY_DATE) DATA_ENTREGA_PO,
TO_CHAR(CASE WHEN (REQUISITION_DETAIL.STATUS='ORDER')
THEN 'COMPRA EM ANDAMENTO'
ELSE
  CASE WHEN (REQUISITION_DETAIL.STATUS='OPEN')
  THEN 'PENDENTE COMPRAS'
  ELSE
    CASE WHEN (REQUISITION_DETAIL.STATUS='CLOSED')
    THEN 'RECEBIDO ALMOX'
    ELSE
      CASE WHEN (REQUISITION_DETAIL.STATUS='CANCEL')
      THEN 'CANCELADO'
      ELSE '-'
      END
    END  
  END
END) SITUACAO,
CASE
WHEN SUBSTR(TO_CHAR(REQUISITION_HEADER.TASK_CARD),0,2) ='NR' THEN TO_CHAR(WO_TASK_CARD.SCHEDULE_TASK_CARD) ELSE TO_CHAR(REQUISITION_HEADER.TASK_CARD) 
END TASK_F,
TO_CHAR('REQUISITION') AS ORIGEM

FROM 
ODB.REQUISITION_DETAIL REQUISITION_DETAIL 
INNER JOIN ODB.REQUISITION_HEADER REQUISITION_HEADER ON REQUISITION_HEADER.REQUISITION = REQUISITION_DETAIL.REQUISITION
LEFT JOIN ODB.WO_TASK_CARD WO_TASK_CARD ON REQUISITION_HEADER.TASK_CARD = WO_TASK_CARD.TASK_CARD AND REQUISITION_HEADER.WO = WO_TASK_CARD.WO
LEFT JOIN ODB.WO ON WO_TASK_CARD.WO = WO.WO
LEFT JOIN ODB.ORDER_DETAIL ON REQUISITION_DETAIL.REQUISITION = ORDER_DETAIL.REQUISITION
AND REQUISITION_DETAIL.REQUISITION_LINE = ORDER_DETAIL.REQUISITION_LINE
LEFT JOIN ODB.ORDER_HEADER ORDER_HEADER ON ORDER_DETAIL.ORDER_NUMBER = ORDER_HEADER.ORDER_NUMBER

LEFT JOIN 
(SELECT DISTINCT
PNALL.PN,
PNALL.PN_DESCRIPTION,
PNALL.CATEGORY,
PNALL.PN_INTERCHANGEABLE,
PNALL.STOCK_UOM

FROM
(SELECT DISTINCT PM.PN, PM.PN_DESCRIPTION, PM.CATEGORY, PI.PN_INTERCHANGEABLE, PM.STOCK_UOM FROM ODB.PN_MASTER PM INNER JOIN
                                                             ODB.PN_INTERCHANGEABLE PI ON PM.PN = PI.PN
UNION

SELECT DISTINCT PI.PN_INTERCHANGEABLE, PM.PN_DESCRIPTION, PM.CATEGORY, PM.PN, PM.STOCK_UOM FROM ODB.PN_MASTER PM 
INNER JOIN ODB.PN_INTERCHANGEABLE PI ON PM.PN = PI.PN) PNALL) PN_MASTER ON PN_MASTER.PN = REQUISITION_DETAIL.PN

WHERE
REQUISITION_HEADER.CREATED_DATE >= SYSDATE-250
AND REQUISITION_DETAIL.LOCATION IN ('PLU','VCP')
AND REQUISITION_HEADER.PRIORITY IN ('CHECK','PLAN','WSP')
AND TO_CHAR(REQUISITION_HEADER.AC) = 'PR-AQK') REQ

LEFT JOIN
(SELECT 
WO,
AC,
PHASE,

CASE
WHEN PHASE = 'MI-01' THEN 'ACCESS OPENING/CLOSING'
WHEN PHASE = 'MI-02' THEN 'AIR CONDITIONING AND APU TEST'
WHEN PHASE = 'MI-03' THEN 'CLEANING'
WHEN PHASE = 'MI-04' THEN 'COCKPIT TEST'
WHEN PHASE = 'MI-05' THEN 'COMPLEMENTARY CHECK'
WHEN PHASE = 'MI-06' THEN 'ENGINEERING ORDERS'
WHEN PHASE = 'MI-07' THEN 'EWIS SPECIAL'
WHEN PHASE = 'MI-08' THEN 'EXTERNAL CLEANING'
WHEN PHASE = 'MI-09' THEN 'FINAL CHECKS'
WHEN PHASE = 'MI-10' THEN 'OPERATIONAL / FUNCTIONAL CHECKS'
WHEN PHASE = 'MI-11' THEN 'INDUCTION AND ARRIVAL TEST'
WHEN PHASE = 'MI-12' THEN 'INTERNAL CLEANING'
WHEN PHASE = 'MI-13' THEN 'LUBRICATION'
WHEN PHASE = 'MI-14' THEN 'AZULTASK'
WHEN PHASE = 'MI-15' THEN 'RIGGING'
WHEN PHASE = 'MI-16' THEN 'SERVICING LANDING GEAR'
WHEN PHASE = 'MI-17' THEN 'SPECIAL ITEMS'
WHEN PHASE = 'MI-18' THEN 'WEIGHTING'
WHEN PHASE = 'MI-19' THEN 'Z100 PRIMARY INSPECTION'
WHEN PHASE = 'MI-20' THEN 'Z200 PRIMARY INSPECTION'
WHEN PHASE = 'MI-21' THEN 'Z300 PRIMARY INSPECTION'
WHEN PHASE = 'MI-22' THEN 'Z400 PRIMARY INSPECTION'
WHEN PHASE = 'MI-23' THEN 'Z500 PRIMARY INSPECTION'
WHEN PHASE = 'MI-24' THEN 'Z600 PRIMARY INSPECTION'
WHEN PHASE = 'MI-25' THEN 'Z700 PRIMARY INSPECTION'
WHEN PHASE = 'MI-26' THEN 'Z800 PRIMARY INSPECTION'
WHEN PHASE = 'MI-27' THEN 'WORK SCOPE REVIEW'
WHEN PHASE = 'MI-28' THEN 'ENGINEERING AUTHORIZATION (EA)'
WHEN PHASE = 'MI-29' THEN 'NON ROUTINE'
WHEN PHASE = 'MI-30' THEN 'Z PRIMARY INSPECTION' END AS MILESTONE_DESCR,

FLOWDAY,
AREA,
SITE,
CASE
WHEN SUBSTR(WO_TASK_CARD.TASK_CARD,0,2) = 'NR' THEN WO_TASK_CARD.SCHEDULE_TASK_CARD ELSE WO_TASK_CARD.TASK_CARD END AS TASK_F
FROM ODB.WO_TASK_CARD 
WHERE 
WO_TASK_CARD.CREATED_DATE >= SYSDATE - 250
AND PHASE IS NOT NULL) PHASE ON REQ.WO = PHASE.WO AND REQ.AC = PHASE.AC AND REQ.TASK_F = PHASE.TASK_F
""")

dfrequire = pd.DataFrame(requiremat, columns = ['TASK_CARD','TASK_CARD_DESCRIPTION','SCHEDULE_TASK_CARD','WO','CHAPTER','ATA_DESCRIPTION','PN','PN_DESCRIPTION','PN_CATEGORY','UOM_PN_MASTER','CATEGORY','PICKLIST','PICKLIST_LINE','PRIORITY','CREATED_DATE','PERIOD','QTY','ORIGINAL_LOCATION','LOCATION','AC','STATUS','NOTES_TEXT','REQUISITION','REQUISITION_DESCRIPTION','AUTHORIZATION','ASSIGN_TO','REQUISITION_TYPE','CRIACAO_RQ','SUM_QTY_AVAILABLE','ORDER_NUMBER','PO_ORACLE','DATA_ENTREGA_PO','SITUACAO','TASK_F','ORIGEM','PHASE','MILESTONE_DESCR','FLOWDAY','AREA','SITE'])

conn.close()

print(dfrequire.head(0))