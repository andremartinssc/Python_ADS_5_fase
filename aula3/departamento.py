class Funcionario:
    def __init__(self, nome: str, cargo: str):
        self.nome = nome
        self.cargo = cargo
        

class Departamento:
    def __init__(self, nome, funcionarios):
        self.nome = nome
        self.funcionarios = funcionarios
    
    def exibir_departamento(self):
        print("Departamento: " + self.nome)
        print("Funcionários:")
        for funcionario in self.funcionarios:
            print("- " + funcionario.nome + " (" + funcionario.cargo + ")")

        
funcionario1 = Funcionario("Pedro", "Vendas")
funcionario2 = Funcionario("Jose", "Estoque")
funcionario3 = Funcionario("Paulo", "RH")

departamento1 = Departamento("RH", [funcionario1, funcionario2, funcionario3])

departamento1.exibir_departamento()