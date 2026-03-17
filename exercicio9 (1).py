class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade 
    
    def calcular_total (self):
        valor_total = self.quantidade * self.preco
        print(f"O valor total em estoque do produto {self.nome} é de R$ {valor_total}")


    def adicioinar_estoque(self):
        if self.quantidade < 0:
            print("Quantidade negativa.")
        
        else:
            quantos = int(input(f"Digite a quantidade de estoque de {self.nome} deseja adicionar:"))
            print(f"Quantidade atual em estoque de {self.nome}: {self.quantidade}")
            self.quantidade = self.quantidade + quantos
            print(f"Foram adicionados {quantos} produto(s) e o estoque atual é de {self.quantidade} produtos(s)")
        
        
    
    def remover_estoque(self):
        remover_quantidade = int(input(f"Digite a quantidade de {self.nome} que deseja remover do estoque: "))
        print(f"Quantidade atual em estoque de {self.nome}: {self.quantidade}")
        self.quantidade = self.quantidade - remover_quantidade
        if self.quantidade < 0:
            print("Quantidade negativa de produtos")
        else:
         print(f"Foram removidos {remover_quantidade} produto(s) e o estoque atual tem {self.quantidade} produto(s)")
        
            
        
    
     
teste1 = Produto("Teclado", 250, 120)
teste2 = Produto("Mouse", 150, 98)


teste1.adicioinar_estoque()
teste1.remover_estoque()
teste1.calcular_total()


teste2.adicioinar_estoque()
teste2.remover_estoque()
teste2.calcular_total()