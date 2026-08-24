class SensorVibracao:
    def __init__(self, id_sensor):
        self.id_sensor = id_sensor
        self.vibracao_atual = 2.3  # em mm/s RMS
        self.limite_maximo = 4.5   # em mm/s RMS

# Criamos uma instância do sensor
sensor_vibracao = SensorVibracao("SENSOR-MOTOR-01")

# 1. ACESSANDO um atributo para verificar a vibração atual
print(f"Vibração atual: {sensor_vibracao.vibracao_atual} mm/s")

# 2. MODIFICANDO um atributo para definir um novo limite
print("Ajustando limite máximo de vibração...")
sensor_vibracao.limite_maximo = 5.0

# 3. VERIFICANDO a mudança
print(f"Novo limite máximo: {sensor_vibracao.limite_maximo} mm/s")