even = [] #lista pra colocar os numeros pares

for num in range(1, 21): #for pra percorrer de 1 a 20
    if (num % 2 == 0):
        even.append(num) #Adicionos os numeros pares na lista

print(even)

how_many = len(even) #vejo quantos numeros possuo na lista

print(f"There are {how_many} even numbers")