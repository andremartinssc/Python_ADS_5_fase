class Livro:
    def __init__(self,titulo: str, autor: str, ano: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def exibir_detalhes(self):
        print(self.titulo, self.autor, self.ano)


livro1 = Livro("A Mumia", "Adam Sandler", 1478)
livro2 = Livro("A Volta dos Que Nao Foram", "Jim Carray", 1995)

livro1.exibir_detalhes()
livro2.exibir_detalhes()