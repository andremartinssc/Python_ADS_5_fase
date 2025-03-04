class Bateria:
    def __init__(self, capacidade):
        self.capacidade = capacidade

class Celular:
    def __init__(self, modelo, capacidade_bateria):
        self.modelo = modelo
        self.bateria = Bateria(capacidade_bateria)

    def exibir_dados(self):
        print(f"Celular: {self.modelo}, Bateria: {self.bateria.capacidade} mAh")

celular1 = Celular("Motorola", 5000)
celular1.exibir_dados()
