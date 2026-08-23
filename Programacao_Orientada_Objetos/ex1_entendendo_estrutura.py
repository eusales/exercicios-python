# Classe com método (ler_temperatura)

class SensorDeTemperatura:
    def __init__(self, id_sensor, localizacao):
        self.id_sensor = id_sensor
        self.localizacao = localizacao
        self.temperatura_atual = 0.0

    # Este é um método
    def ler_temperatura(self, nova_leitura):
        self.temperatura_atual = nova_leitura
        print(f"Sensor {self.id_sensor}: Temperatura atualizada para {self.temperatura_atual}°C")


# Objetos (instâncias) e acesso aos atributos

# Criando objetos (instâncias) a partir da classe "SensorDeTemperatura"
sensor_01 = SensorDeTemperatura("ID-A01", "Motor Principal")
sensor_02 = SensorDeTemperatura("ID-B02", "Esteira de Saída")

# Cada objeto tem seus próprios dados (atributos)
print(f"Sensor: {sensor_01.id_sensor}, Local: {sensor_01.localizacao}")
print(f"Sensor: {sensor_02.id_sensor}, Local: {sensor_02.localizacao}")

# Exemplo de uso do método
sensor_01.ler_temperatura(28.6)
sensor_02.ler_temperatura(31.2)