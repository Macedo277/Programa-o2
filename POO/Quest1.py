# 1. Suponha que você está desenvolvendo um sistema de biblioteca. Crie a
# classe Livro com as seguintes características:
# ○ Atributos: titulo, autor, ano_publicacao.
# ○ Métodos: exibir_detalhes


class livro:
    def ___init__(self, titulo, autor, ano):
        self.nome_do_livro = titulo
        self.nome_autor = autor
        self.ano_publicação = ano
        
    def exibir_detalhes(self):
        print(f"Título: {self.nome_do_livro}.\n Autor:
        {self.nome_autor}.\n Ano de publicação: {self.ano_publicação}.")

Book1 = livro("Rambo", "Sylvester Stalone", '1997')
Book2 = livro("Chaves", "Roberto Gomes Bolãnos", '1950')

print(f"O nome do livro 1 é: {Book1.nome_do_livro}")