numero = int(input("De qual tabuada deseja: "))

multiplicador = 1

while True:

        conta = numero * multiplicador
        print(f"{numero} x {multiplicador} = {conta}")
        multiplicador += 1


        if multiplicador > 10:
            break


"""
Boas Praticas: numero = int(input("De qual tabuada deseja: "))

# O 'range(1, 11)' gera números de 1 a 10 (o segundo valor é exclusivo)
for multiplicador in range(1, 11):
    conta = numero * multiplicador
    print(f"{numero} x {multiplicador} = {conta}")
"""