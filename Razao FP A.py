import os
import pandas as pd

os.chdir(r'C:\Users\paulo.roberto\Documents\Razão VP Tec')
path = r'C:\Users\paulo.roberto\Documents\Razão VP Tec'
listrazao = []
listaok = []
listatratada = []
conta = 0

for arq in os.listdir(path):

    with open('{}'.format(arq),encoding='ANSI') as razao:
        razao = razao.readlines()
        for row in (razao):
            listrazao.append(row)

    for linha in razao:
        contagem = linha.count(';')

        if contagem == 78:
            listaok.append(linha)

    for linha in listrazao:
        contagem = linha.count(';')
        if contagem < 78:
            if listrazao[conta].count(';') + listrazao[conta+1].count(';') == 78:
                rowap1 = listrazao[conta]+listrazao[conta+1]
                listatratada.append(rowap1)
            if listrazao[conta].count(';') + listrazao[conta+1].count(';') + listrazao[conta+2].count(';') == 78:
                rowap2 = listrazao[conta] + listrazao[conta + 1]+ listrazao[conta + 2]
                listatratada.append(rowap2)
            conta += 1

listafim = listaok + listatratada

count = 0

for i in listafim:
    listafim[count] = i.split(';')
    count += 1

Filial=[Filial[3] for Filial in listafim[1:len(listafim)]]
Descrição_Filial=[Descrição_Filial[4] for Descrição_Filial in listafim[1:len(listafim)]]
Centro_de_Custo=[Centro_de_Custo[5] for Centro_de_Custo in listafim[1:len(listafim)]]
Descrição_Centro_de_Custo=[Descrição_Centro_de_Custo[6] for Descrição_Centro_de_Custo in listafim[1:len(listafim)]]
Conta=[Conta[7] for Conta in listafim[1:len(listafim)]]
Descrição_Conta=[Descrição_Conta[8] for Descrição_Conta in listafim[1:len(listafim)]]
Tipo_de_Aeronave=[Tipo_de_Aeronave[9] for Tipo_de_Aeronave in listafim[1:len(listafim)]]
Descrição_Tipo_de_Aeronave=[Descrição_Tipo_de_Aeronave[10] for Descrição_Tipo_de_Aeronave in listafim[1:len(listafim)]]
Tipo_de_Servico=[Tipo_de_Servico[13] for Tipo_de_Servico in listafim[1:len(listafim)]]
Descrição_Tipo_de_Servico=[Descrição_Tipo_de_Servico[14] for Descrição_Tipo_de_Servico in listafim[1:len(listafim)]]
Prefixo_da_Aeronave=[Prefixo_da_Aeronave[15] for Prefixo_da_Aeronave in listafim[1:len(listafim)]]
Descrição_Prefixo_da_Aeronave=[Descrição_Prefixo_da_Aeronave[16] for Descrição_Prefixo_da_Aeronave in listafim[1:len(listafim)]]
Líquido=[Líquido[19] for Líquido in listafim[1:len(listafim)]]
Mês=[Mês[20] for Mês in listafim[1:len(listafim)]]
Data_GL=[Data_GL[21] for Data_GL in listafim[1:len(listafim)]]
Origem=[Origem[22] for Origem in listafim[1:len(listafim)]]
Categoria=[Categoria[23] for Categoria in listafim[1:len(listafim)]]
Histórico=[Histórico[24] for Histórico in listafim[1:len(listafim)]]
Moeda=[Moeda[29] for Moeda in listafim[1:len(listafim)]]
Fornecedor=[Fornecedor[36] for Fornecedor in listafim[1:len(listafim)]]
Numero_NF_RIAP=[Numero_NF_RIAP[42] for Numero_NF_RIAP in listafim[1:len(listafim)]]
Criador_RIAP=[Criador_RIAP[48] for Criador_RIAP in listafim[1:len(listafim)]]
Observacoes_da_Aprovacao_PO=[Observacoes_da_Aprovacao_PO[56] for Observacoes_da_Aprovacao_PO in listafim[1:len(listafim)]]

df = pd.DataFrame(list(zip(Filial,Descrição_Filial,Centro_de_Custo,Descrição_Centro_de_Custo,Conta,Descrição_Conta,Tipo_de_Aeronave,Descrição_Tipo_de_Aeronave,Tipo_de_Servico,Descrição_Tipo_de_Servico,Prefixo_da_Aeronave,Descrição_Prefixo_da_Aeronave,Líquido,Mês,Data_GL,Origem,Categoria,Histórico,Moeda,Fornecedor,Numero_NF_RIAP,Criador_RIAP,Observacoes_da_Aprovacao_PO)), columns=['Filial','Descrição_Filial','Centro_de_Custo','Descrição_Centro_de_Custo','Conta','Descrição_Conta','Tipo_de_Aeronave','Descrição_Tipo_de_Aeronave','Tipo_de_Servico','Descrição_Tipo_de_Servico','Prefixo_da_Aeronave','Descrição_Prefixo_da_Aeronave','Líquido','Mês','Data_GL','Origem','Categoria','Histórico','Moeda','Fornecedor','Numero_NF_RIAP','Criador_RIAP','Observacoes_da_Aprovacao_PO'])
