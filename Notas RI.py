print('Digite "NÃO" caso queira encerrar a pesquisa')
pesquisa = input('Digite o que deseja pesquisar: ')
lista = []

while pesquisa != 'NÃO':#esquanto a pesquisa for diferente de "NÃO"
    lista.append(pesquisa)#Complementa a lista com a pesquisa
    pesquisa = input('Digite o que deseja pesquisar: ')#Insere nova palavra a ser pesquisada

    with open(r"C:\Users\paulo.roberto\Documents\NFs RI - Out 2019.txt",'r', encoding='utf-8', errors='surrogateescape') as NotasRI :#Abre arquivo para pesquisar
        header = ''
        for cabecalho in NotasRI:
            if cabecalho.startswith('EMPRESA;'):
                header = cabecalho
                with open(r"C:\Users\paulo.roberto\Documents\{}.txt".format('AnaliseRI'), 'w', encoding='utf-8', errors='surrogateescape') as AnaliseRI:  # Cria novo arquivo para escrever a pesquisa
                    AnaliseRI.write('Classe;' + header)  # Escreve o cabeçalho
                    for linha in NotasRI:  # Corre cada linha do arquivo
                        for item in lista:  # Para cada item da lista criada
                            if linha.__contains__(item):  # Se a linha do txt aberto conter o item da lista criada vai escrever o nome do item + a linha que contem tal item
                                AnaliseRI.write(item + ";" + linha)
