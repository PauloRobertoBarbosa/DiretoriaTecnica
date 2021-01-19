# file = open(r"C:\Users\paulo.roberto\Documents\Realizado 2019 VP tecnica.txt",'r', encoding='utf-8', errors='surrogateescape')
# cont = 0
# header = ''
# for linha in file:
#     cont = cont + 1
#     if linha.startswith('Lote;'):
#         header = linha
#
# file.close()
#
# with open(r"C:\Users\paulo.roberto\Documents\Realizado 2019 VP tecnica.txt",'r', encoding='utf-8', errors='surrogateescape') as razao :
#     newfile = input('Digite o nome do Arquivo : ')
#     pesquisa = str(newfile).rstrip().lstrip()
#     with open(r"C:\Users\paulo.roberto\Documents\{}.txt".format(newfile), 'w', encoding='utf-8', errors='surrogateescape') as newfile:
#         newfile.write('Classe;' + header)
#         for linha in razao:
#             if linha.__contains__(pesquisa):
#                 newfile.write(pesquisa+";"+linha)


print('Digite "NÃO" caso queira encerrar a pesquisa')
pesquisa = input('Digite o que deseja pesquisar: ')
lista = []

while pesquisa != 'NÃO':#esquanto a pesquisa for diferente de "NÃO"
    lista.append(pesquisa)#Complementa a lista com a pesquisa
    pesquisa = input('Digite o que deseja pesquisar: ')#Insere nova palavra a ser pesquisada

    with open(r"C:\Users\paulo.roberto\Documents\Realizado 2019 VP tecnica.txt",'r', encoding='utf-8', errors='surrogateescape') as Razao :#Abre arquivo para pesquisar
        header = ''
        for cabecalho in Razao:
            if cabecalho.startswith('Lote;'):
                header = cabecalho  
                with open(r"C:\Users\paulo.roberto\Documents\{}.txt".format('AnaliseCheck'), 'w', encoding='utf-8', errors='surrogateescape') as AnaliseHeavy:  # Cria novo arquivo para escrever a pesquisa
                    AnaliseHeavy.write('Classe;' + header)  # Escreve o cabeçalho
                    for linha in Razao:  # Corre cada linha do arquivo
                        for item in lista:  # Para cada item da lista criada
                            if linha.__contains__(item):  # Se a linha do txt aberto conter o item da lista criada vai escrever o nome do item + a linha que contem tal item
                                AnaliseHeavy.write(item + ";" + linha)