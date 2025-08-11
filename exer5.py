"""
Exercício 5: Palíndromo
Crie um programa que solicite ao usuário uma palavra e verifique se ela é um palíndromo. Um palíndromo é uma palavra que se lê da mesma forma de trás para frente.

Exemplos:

Palíndromos: arara, ovo, reviver, socos

Não palíndromos: python, casa, computador

Dicas:

Lembre-se de remover espaços e considerar a palavra em letras minúsculas para evitar erros de comparação (ex: "A Torta" e "atorta").

Uma maneira de inverter uma string em Python é usando o slicing de string: palavra[::-1].

"""
while True:

    palavra = input("Qual é a palavra: ")

    inverter = palavra[::-1]

    if (palavra.lower() == inverter.lower()):
        print("A palavra é um Palíndromo.")

    else:
        print("A palavra não é um Palíndromo.")
    
