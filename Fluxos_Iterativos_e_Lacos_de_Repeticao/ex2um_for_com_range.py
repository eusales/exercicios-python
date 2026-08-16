#Exemplo 1 – Usando for com range()

# O loop irá iterar de 1 a 5, representando cada ciclo de consumo
for ciclo in range(1, 6):
    # Cálculo do consumo de energia para o ciclo atual
    consumo = 50 + (ciclo * 8)
    # Exibe o ciclo e o respectivo consumo de energia em kW
    print(f"Ciclo {ciclo}: Consumo de energia = {consumo} kW")