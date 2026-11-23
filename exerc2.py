class Livro:
    def __init__(self, titulo, autor, ano_publicacao, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.isbn = isbn
        self.disponivel = True 

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado no momento.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido e está disponível.")
        else:
            print(f"O livro '{self.titulo}' já consta como disponível na biblioteca.")

    def exibir_informacoes(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"Título: {self.titulo} | Autor: {self.autor} ({self.ano_publicacao}) | Status: {status}")

livro1 = Livro("As aventuras de Pedrão", "Machado de Assis", 1899, "978-8535910663")

livro1.exibir_informacoes()
livro1.emprestar()
livro1.exibir_informacoes()
livro1.devolver()