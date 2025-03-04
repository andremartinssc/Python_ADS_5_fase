class Carro:
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, aumento):
        self.velocidade += aumento
        return self.velocidade
    
    def frear(self, reducao):
        self.velocidade -= reducao
        if self.velocidade < 0:
            self.velocidade = 0
        return self.velocidade
    
    def mostrar_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}, Velocidade:{self.velocidade} km/h")