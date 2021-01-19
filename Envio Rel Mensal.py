import os
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')

CC = ['2300','2301','2302','2305','2307','2308','2310','2315','2320','2321','2322','2323','2325','2326','2327','2328','2330','2331',
      '2340','2370','2372','2380','2400','2401','2402','2403','2404','2405','2406','2407','2420','2430','2431']
dest = ["","","","Fabio Stersi Damasceno <fabio.damasceno@voeazul.com.br>; Antonio de Jesus Vieira <antonio.vieira@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Antonio Augusto de Azevedo Eick <antonio.eick@voeazul.com.br>;Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>","",
        "Vinicius Almeida <vinicius.almeida@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Sergio Videira <sergio.videira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Paulo Okubo <paulo.okubo@voeazul.com.br>; Reuel Matos <reuel.matos@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Gilson Burman <gilson.burman@voeazul.com.br>; Reuel Matos <reuel.matos@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Paulo Okubo <paulo.okubo@voeazul.com.br>; Augusto Martins Rossetti <augusto.rossetti@voeazul.com.br>; Reuel Matos <reuel.matos@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Alberto Ottavio Spelta <alberto.spelta@voeazul.com.br>; Reuel Matos <reuel.matos@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Plinio Antonio Silva de Oliveira <plinio.oliveira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Plinio Antonio Silva de Oliveira <plinio.oliveira@voeazul.com.br>; Luiz Sergio Barbosa Junior <luiz.barbosa@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>","","",
        "Antonio Pisco Carraça <antonio.carraca@voeazul.com.br>; Carlos Jose Lisboa <carlos.lisboa@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Juliane Silva Fávaro <Juliane.Favaro@voeazul.com.br>;Elisangela Rodrigues Martinez <elisangela.martinez@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Carlos Cesar Nunes de Senna Facundo <carlos.facundo@voeazul.com.br>; Antonio Pisco Carraça <antonio.carraca@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Daniel Fernandes Dutra Junior <daniel.dutra@voeazul.com.br>; Antonio Pisco Carraça <antonio.carraca@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Antonio Pisco Carraça <antonio.carraca@voeazul.com.br>; Antonio de Jesus Vieira <antonio.vieira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Renan Dapena Roveran <renan.roveran@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>; Generson Silva Oliveira <generson.oliveira@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Ricardo Luiz Vasconcellos <ricardo.vasconcellos@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Davidson Geraldo Ferreira <davidson.ferreira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Davidson Geraldo Ferreira <davidson.ferreira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Davidson Geraldo Ferreira <davidson.ferreira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Davidson Geraldo Ferreira <davidson.ferreira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Davidson Geraldo Ferreira <davidson.ferreira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Davidson Geraldo Ferreira <davidson.ferreira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Davidson Geraldo Ferreira <davidson.ferreira@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Álvaro Luis da Silva Garcia <alvaro.garcia@voeazul.com.br>; Antonio Augusto de Azevedo Eick <antonio.eick@voeazul.com.br>;Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Renato Tezoto <Renato.Tezoto@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Antonio Pisco Carraça <antonio.carraca@voeazul.com.br>; Cileno Ribeiro De Castro <cileno.castro@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>",
        "Antonio Pisco Carraça <antonio.carraca@voeazul.com.br>; Carlos Alexandre Naufel <carlos.naufel@voeazul.com.br>; Elzinete Ramos da Costa <elzinete.costa@voeazul.com.br>;Marilia Almeida Mattos Mendonça Garcia <marilia.garcia@voeazul.com.br>;Mateus P. Guimarães <mateus.pguimaraes@voeazul.com.br>"]

count = 0

os.chdir(r'C:\Users\paulo.roberto\Documents\Arquivos PDF\Analise Mensal Realizado\jul 2020')

path = r"C:\Users\paulo.roberto\Documents\Arquivos PDF\Analise Mensal Realizado\jul 2020"
for i in os.listdir():
    if i.__contains__(CC[count]):
        mail = outlook.CreateItem(0)
        mail.To = dest[count]
        mail.Subject = "Acompanhamento Orçamentário - {} - jul - 2020".format(CC[count])
        mail.HtmlBody = str("""
Bom dia !<br>
<br>
Segue relatório de Acompanhamento Orçamentário referente ao mês de julho de 2020.<br>
<br>
O relatório também está disponível no link:<br>
<br>
<a href="https://app.powerbi.com/groups/b3fa47de-cb1e-4dc0-bca0-b2a48725ec8b/reports/eec161b4-5cff-41fe-b98e-5ec907c6700b/ReportSectiona916aaf2ddca52c5e200">Análise Mensal Realizado</a> <br>
<br>
Se o site solicitar algum acesso extra peço que me informe.<br>
<br>
Qualquer dúvida estou à disposição.<br>
<br>
Att
""")
        fullpath = os.path.abspath(i)
        mail.Attachments.Add(fullpath)
        mail.Display(True)
        count += 1
    else: pass