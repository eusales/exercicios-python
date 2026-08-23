class RoboIndustrial:
    def __init__(self, id_robo, ferramenta_inicial):
        self.id_robo = id_robo
        self.ferramenta_atual = ferramenta_inicial
        self.status = "em espera"

    # Método (Comportamento) para mudar o status
    def ativar(self):
        print(f"Robô {self.id_robo} ativando...")
        self.status = "ativo" # O método altera o próprio atributo do objeto

    # Método para trocar a ferramenta
    def trocar_ferramenta(self, nova_ferramenta):
        self.ferramenta_atual = nova_ferramenta
        print(f"Robô {self.id_robo} trocou para a ferramenta: {self.ferramenta_atual}")


# Criando duas instâncias (objetos) da classe RoboIndustrial
robo_A = RoboIndustrial("R-A01", "garra")
robo_B = RoboIndustrial("R-B02", "soldador")

# Verificando os atributos iniciais de cada um
print(f"Status inicial do {robo_A.id_robo}: {robo_A.status}")
print(f"Status inicial do {robo_B.id_robo}: {robo_B.status}")

# Agora, vamos fazer o robo_A realizar uma ação
robo_A.ativar()

# Verificando os status novamente
print(f"Novo status do {robo_A.id_robo}: {robo_A.status}")
print(f"Status do {robo_B.id_robo} (não foi alterado): {robo_B.status}")