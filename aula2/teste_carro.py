from carro import Carro

carro1 = Carro("Toyota", "corola", 2022)
carro2 = Carro("Honda", "Civic", 2021)

carro1.mostrar_detalhes()
carro2.mostrar_detalhes()

carro1.acelerar(50)
carro1.frear(20)
carro1.mostrar_detalhes()
print("Fim do teste")


