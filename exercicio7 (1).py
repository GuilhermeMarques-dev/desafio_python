produtos = [
 {"nome": "Mouse", "quantidade": 10, "preco": 50.0},
{"nome": "Teclado", "quantidade": 5, "preco": 120.0}
]

def exibir_produtos(produtos):  
    nome_produtos = []
    for produtos in produtos:
        nome_produtos.append(produtos["nome"])

    print(f"Os produtos existentes são {nome_produtos}")



def calcular_valor_produtos(produtos):
    produto_escolhido =  input("Digite qual produto deseja saber o valor total estocado: ").upper()
    achado = False 
    
    for produto in produtos:
       
       if produto["nome"].upper() == produto_escolhido:
           valor_total = produto["quantidade"] * produto["preco"]
           print(f"O valor total do produto {produto["nome"]} em estoque é de R$ {valor_total:.2f}")
           achado = True
           break
       
    if not achado:
        print("Produto não encontrado.")
    


def calcular_total_estoque(produtos):
    valor_total_estoque = 0
    for produto in produtos:
     valor_total_estoque += produto["quantidade"] * produto["preco"]
     
    print(f"O valor total do estoque é de R$ {valor_total_estoque:.2f}")



exibir_produtos(produtos)
calcular_valor_produtos(produtos)
calcular_total_estoque(produtos)