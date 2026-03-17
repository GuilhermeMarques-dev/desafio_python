# tava fazendo em ingles mas fiquei com preguiça
numero = float(input("Digite um numero:"))
def analisar_numero(numero):  # função direcionando pra variável numero 
    if numero == 0:
        print("Numero igual a zero")
    elif numero < 0:
        print("Numero negativo")
    else:
        print("Numero positivo")
# Linhas 4 a 9 são as condiçoes analizando o numero
analisar_numero(numero)