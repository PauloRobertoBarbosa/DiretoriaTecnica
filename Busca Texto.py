print('Digite "NÃO" caso queira encerrar a pesquisa')
arquvivo = input('Digite o arquivo com a extensão')
pesquisa = input('Digite o que deseja pesquisar: ')
lista = []


while pesquisa != 'NÃO':#esquanto a pesquisa for diferente de "NÃO"
    lista.append(pesquisa)#Complementa a lista com a pesquisa
    pesquisa = input('Digite o que deseja pesquisar: ')#Insere nova palavra a ser pesquisada
#
for i in lista:
    with open(r"C:\Users\paulo.roberto\Documents\Base Razao\{}".format(arquvivo),'r', encoding='utf-8', errors='surrogateescape') as buscatxt :#Abre arquivo para pesquisar
        header = ''
        for cabecalho in buscatxt:
            if cabecalho.startswith('Lote;'):
                header = cabecalho
                with open(r"C:\Users\paulo.roberto\Documents\{}.txt".format('buscatxt'), 'w', encoding='utf-8', errors='surrogateescape') as buscatxtpesquisa:  # Cria novo arquivo para escrever a pesquisa
                    buscatxtpesquisa.write('Classe;' + header)  # Escreve o cabeçalho
                    for linha in buscatxt:  # Corre cada linha do arquivo
                        for item in lista:  # Para cada item da lista criada
                            if linha.__contains__(item):  # Se a linha do txt aberto conter o item da lista criada vai escrever o nome do item + a linha que contem tal item
                                buscatxtpesquisa.write(item + ";" + linha)