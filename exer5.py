"""
Crie um programa que solicite ao usuário uma palavra e verifique se ela é um palíndromo. Um palíndromo é uma palavra que se lê da mesma forma de trás para frente.

Exemplos:

Palíndromos: arara, ovo, reviver, socos

"""
while True:

    palavra = input("Qual é a palavra: ")

    inverter = palavra[::-1]

    if (palavra.lower() == inverter.lower()):
        print("A palavra é um Palíndromo.")

    else:
        print("A palavra não é um Palíndromo.")
    
