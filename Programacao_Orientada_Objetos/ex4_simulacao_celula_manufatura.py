class Esteira:
    def __init__(self, id_esteira):
        self.id = id_esteira
        self.status = "parada" # Status inicial

    def ligar(self):
        self.status = "movendo"
        print(f"Esteira {self.id}: movendo.")

    def parar(self):
        self.status = "parada"
        print(f"Esteira {self.id}: parada para acesso do robô.")


class Robo:
    def __init__(self, id_robo):
        self.id = id_robo
        self.status = "em espera"

    def pegar_peca(self, esteira_alvo):
        print(f"Robô {self.id}: iniciando operação de coleta.")
        self.status = "trabalhando"

        # INTERAÇÃO: O robô ACESSA o atributo da esteira
        if esteira_alvo.status == "movendo":
            print(f"Robô {self.id}: a esteira está movendo. Solicitando parada...")
            # INTERAÇÃO: O robô CHAMA o método da esteira
            esteira_alvo.parar()

        print(f"Robô {self.id}: pegando a peça da esteira {esteira_alvo.id}.")
        # Lógica para pegar a peça aqui...
        print(f"Robô {self.id}: peça coletada com sucesso.")
        self.status = "em espera"


esteira_producao = Esteira("EST-01")
robo_braco = Robo("RB-01")

# 1. Ligamos a esteira
esteira_producao.ligar()

# 2. O robô tenta pegar a peça, interagindo com a esteira
robo_braco.pegar_peca(esteira_producao)

# 3. Verificamos o estado final da esteira
print(f"Estado final da esteira {esteira_producao.id}: {esteira_producao.status}")