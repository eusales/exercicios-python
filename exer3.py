#Crie um programa que solicite ao usuário um número inteiro e, em seguida, imprima uma mensagem dizendo se o número é par ou ímpar.

#Dica: Você pode usar o operador de módulo (%) para verificar o resto da divisão de um número por 2. Se o resto for 0, o número é par.

numero = int(input("Insira um numero inteiro: "))

if numero % 2 == 0:
    print("Eh par")
else:
    print("Eh impar")