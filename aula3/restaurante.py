class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self):
        self.lista_pedidos = [] 
    
    def adicionar_produto(self, produto_adicionado):
        self.lista_pedidos.append(produto_adicionado)
        
    def exibir_pedido(self):
        soma = 0
        for produto in self.lista_pedidos:
            
            soma = produto.preco + soma
            print(produto.nome, "- R$", produto.preco)
            
        print("Total: ", soma)


produto1 = Produto("Bife", 20.0)
produto2 = Produto("Frango", 15.0)
produto3 = Produto("Peixe", 10.0)

pedido1 = Pedido()
pedido1.adicionar_produto(produto1)
pedido1.adicionar_produto(produto2)
pedido1.adicionar_produto(produto3)

pedido1.exibir_pedido()

