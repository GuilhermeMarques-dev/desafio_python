class Livro:
    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    def __str__(self):
        status = "Disponível" if self.disponivel else "emprestado"
        return f"{self.titulo} - {self.autor} - {status}"

class Biblioteca:
    def __init__ (self):
        self.livros = []
    
    def Adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"O livro {livro.titulo} foi adicionado")
    

    def listar_livros(self):
        print("--------------Catálogo----------")
        for livro in self.livros:
            print(livro)



    def emprestar_livros(self, titulo_requerido):
        for livro in self.livros:
            if livro.titulo.lower() == titulo_requerido.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"O livro {livro.titulo} foi emprestado.")
                    return
                else:
                    print(f"O livro {livro.titulo} ja está emprestado. ")
                    return
        print(f"Livro {titulo_requerido} não presente na biblioteca.")    
    
    def devolver_livros(self, titulo_requerido):
        for livro in self.livros:
            if livro.titulo.lower() == titulo_requerido.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"O livro {livro.titulo} foi devolvido")
                    return
                else:
                    print(f"O livro {livro.titulo} ja está disponível. ")
                    return
        print(f"Livro {titulo_requerido} não presente na biblioteca.")    




biblioteca_teste = Biblioteca()
livro1 = Livro("Dom casmurro", "Machado de Assis")
livro2 = Livro("Harry potter", "J.K Rolling")
livro3 = Livro("Biblia", "?")

biblioteca_teste.Adicionar_livro(livro1)
biblioteca_teste.Adicionar_livro(livro2)




biblioteca_teste.listar_livros()
biblioteca_teste.emprestar_livros("Biblia")
biblioteca_teste.Adicionar_livro(livro3)
biblioteca_teste.emprestar_livros("Biblia")
biblioteca_teste.listar_livros()
biblioteca_teste.devolver_livros("Biblia")
biblioteca_teste.listar_livros()







