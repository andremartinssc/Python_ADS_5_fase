class Animal:
    def __init__(self, tipo):
        self.tipo = tipo
    def fazer_som(self):
            pass

class Gato(Animal):
    def __init__(self, tipo):
        super().__init__(tipo)
    def fazer_som(self):
        print("O animal do tipo " + self.tipo + " Miou")
            
class Cachorro(Animal):
    def __init__(self, tipo):
        super().__init__(tipo)
    def fazer_som(self):
        print("O animal do tipo " + self.tipo + " Latiu")
                      
gato1 = Gato("Gato")
cachorro1 = Cachorro("Cachorro")
gato1.fazer_som()
cachorro1.fazer_som()