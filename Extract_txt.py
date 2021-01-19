print('Digite "NÃO" caso queira encerrar a pesquisa')
pesquisa = input('Digite o que deseja pesquisar: ')
lista = []

while pesquisa != 'NÃO':#esquanto a pesquisa for diferente de "NÃO"
    lista.append(pesquisa)#Complementa a lista com a pesquisa
    pesquisa = input('Digite o que deseja pesquisar: ')#Insere nova palavra a ser pesquisada

with open(r"C:\Users\paulo.roberto\Documents\Realizado 2019 VP tecnica.txt",'r', encoding='utf-8', errors='surrogateescape') as POline :#Abre arquivo para pesquisar
    header = ''
    for cabecalho in POline:
        if cabecalho.startswith('Lote;'):
            header = cabecalho
            with open(r"C:\Users\paulo.roberto\Documents\{}.txt".format('Pesquisarazao'), 'w', encoding='utf-8',
                      errors='surrogateescape') as PesquisaPython:  # Cria novo arquivo para escrever a pesquisa
                PesquisaPython.write('Classe;' + header)  # Escreve o cabeçalho
                for linha in POline:  # Corre cada linha do arquivo
                    for item in lista:  # Para cada item da lista criada
                        if linha.__contains__(item):  # Se a linha do txt aberto conter o item da lista criada vai escrever o nome do item + a linha que contem tal item
                            PesquisaPython.write(item + ";" + linha)
