
"""
# Exercício 3: Escreva um programa que solicite ao usuário as horas trabalhadas e o valor por hora para calcular o salário bruto.

hours = input("Enter Hours:") 

rate = input("Enter Rate:")

hours_number = float(hours)
rate_number = float(rate)


print("Pay =", hours_number * rate_number)

"""
#---------------------------------------------------------------------------------------------------------------
"""
Exercício 4: Suponha que executemos as seguintes instruções de atribuição:

width = 17
height = 12.0
Para cada uma das expressões a seguir, escreva o valor da expressão e o tipo (do valor da expressão).

width//2

width/2.0

height/3

1 + 2 * 5
-------------------------
width = 17
height = 12.

Expressao_1 = width//2
Expressao_2 = width/2.0
Expressao_3 = height/3
Expressao_4 = 1 + 2 * 5


print("Expressão 1 =", Expressao_1)
print(type(Expressao_1))
print("Expressão 2 =", Expressao_2)
print(type(Expressao_2))
print("Expressão 3 =", Expressao_3)
print(type(Expressao_3))
print("Expressão 4 =", Expressao_4)
print(type(Expressao_4))

"""
#---------------------------------------------------------------------
"""
Exercício 5: Escreva um programa que solicite ao usuário uma temperatura em Celsius, converta a temperatura para Fahrenheit e imprima a temperatura convertida.
"""
temp_celcius = input("Temperatura em graus Celsius:")
temp_celcius_number = float(temp_celcius)

temp_fahrenheit = (temp_celcius_number * 1.8) + 32

print("Em Fahrenheit:", temp_fahrenheit)
