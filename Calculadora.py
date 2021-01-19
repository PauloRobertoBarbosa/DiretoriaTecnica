import sys

####Boas vindas############
print("""Olá, seja bem vindo a calculadora em Python!
Abaixo os tipos de operações possíveis:
1) Adição
2) Subtração
3) Multiplicação
4) Divisão""")

listaopr = [1,2,3,4]

tipoopr = input("Selecione o tipo de operação desejada :")

if int(tipoopr) not in listaopr:
    sys.exit("Opção Inválida!Tente novamente.")

numa = float(input("Primeiro valor :"))
numb = float(input("Segundo Valor"))

if int(tipoopr) ==1:
    #Adição
    def adicao(a, b):
        a = numa
        b =numb
        print(a + b)
    print("A soma de {} + {} é: ".format(numa, numb))
    adicao(numa,numb)

elif int(tipoopr) ==2:
    #Subtração
    def subtracao(a, b):
        a = numa
        b =numb
        print(a - b)
    print("A subtração de {} - {} é: ".format(numa, numb))
    subtracao(numa,numb)

elif int(tipoopr) == 3:
    #Multipliação
    def multiplicacao(a, b):
        a = numa
        b =numb
        print(a * b)
    print("A mulplicação de {} e {} é: ".format(numa, numb))
    multiplicacao(numa,numb)
elif int(tipoopr)==4:
    #Divisão
    def divisao(a, b):
        a = numa
        b =numb
        print(a / b)
    print("A divisão entre {} e {} é: ".format(numa, numb))
    divisao(numa,numb)