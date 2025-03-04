class Cliente:
    def __init__(self,nome: str, cpf: int):
        self.nome = nome
        self.cpf = cpf
    
class Conta:
    def __init__(self,saldo , cliente):

        self.saldo = saldo
        self.cliente = cliente
        
    def exibir_saldo(self):
        print(self.saldo, self.cliente.nome, self.cliente.cpf)


cliente1 = Cliente("Jose", 99999)
conta1 = Conta(1000, cliente1)

conta1.exibir_saldo()