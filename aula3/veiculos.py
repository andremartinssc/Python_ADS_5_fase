class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo
    def mover(self):
        pass
    
class Bicicleta(Veiculo):
    def __init__(self, tipo):
        super().__init__(tipo)
    def mover(self):
            print("O objeto do tipo " + self.tipo + " anda devagar")
        
class Carro(Veiculo):
    def __init__(self, tipo):
        super().__init__(tipo)
    def mover(self):
            print("O objeto do tipo " + self.tipo + " anda rapido")
    
carro1 = Carro("Carro")
bicicleta1 = Bicicleta("Bicicleta")

carro1.mover()
bicicleta1.mover()