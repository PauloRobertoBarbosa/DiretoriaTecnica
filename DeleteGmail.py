import pandas as pd
import imaplib
import email
import os

os.chdir(r'C:/Users/paulo.roberto/Documents/Arquivos XLS')

FROM_EMAIL = "paulo.r.o.barbosa@gmail.com"
FROM_PWD = "Sophi@031214"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL, FROM_PWD)
mail.select('"Emprega Campinas"', readonly=False)

type_mail, data = mail.search(None, 'ALL')
mail_ids = data[0]

id_list = mail_ids.split()
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])

# for i in id_list:
#     mail.store("{}".format(int(i)), '+X-GM-LABELS', '\\Trash')
mail.store("1:*",'+X-GM-LABELS', '\\Trash')
# print(latest_email_id)
