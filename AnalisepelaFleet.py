with open(r"C:\Users\paulo.roberto\Documents\Fleet.txt",'r', encoding='utf-8', errors='surrogateescape') as fleet:
    Listafleet = []
    for acft in fleet:
        Listafleet.append(str(acft).strip())

with open(r"C:\Users\paulo.roberto\Documents\Realizado 2019 VP tecnica.txt",'r', encoding='utf-8', errors='surrogateescape') as Razao :#Abre arquivo para pesquisar
    header = ''
    for cabecalho in Razao:
        if cabecalho.startswith('Lote;'):
            header = cabecalho
            with open(r"C:\Users\paulo.roberto\Documents\{}.txt".format('AnaliseCheck'), 'w', encoding='utf-8', errors='surrogateescape') as AnaliseHeavy:  # Cria novo arquivo para escrever a pesquisa
                AnaliseHeavy.write('Classe;' + header)  # Escreve o cabeçalho
                for linha in Razao:  # Corre cada linha do arquivo
                    for acft in Listafleet:
                        if linha.__contains__(acft):
                            AnaliseHeavy.write(acft+';'+linha)


