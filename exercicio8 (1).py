vendas = [100, 250, 80, 320, 150]

def resumo_vendas(vendas):
    if len(vendas) == 0:
        print("Não foi registrada nenhuma venda.")
    else:    
     total_vendido = sum(vendas)
     maior_venda =  max(vendas)
     menor_venda = min(vendas)
     media_vendas = total_vendido / len(vendas)
     print(f"Os valores das vendas são: {vendas}")
     print(f"O total vendido foi de {total_vendido} ")
     print(f"A maior venda teve um valor de R$ {maior_venda}")
     print(f"A menor venda teve um valor de R$ {menor_venda}")
     print(f"A media das vendas foi de R$ {media_vendas}")


resumo_vendas(vendas)