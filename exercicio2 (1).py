total = 0
# Aqui eu pensei em fazer um for pra não ter que declarar mt variavel
for i in range(1, 4):
    grade = float(input(f"Enter the {i} grade: \n"))
    total += grade 


average = round(total / 3, 2) #arredondando

# Saindo do for exibi o resultado da  media e dps fiz verifiaçãod e aprovado ou não
print(f"Your avarage grade was {average:.2f}")
if (average >= 7):
    print("Approved")
elif (average > 5 and average <= 6.9):
    print("Recovery")

else:
    print("Reproved")


#Aqui ia partir da linha 2 ate a linha 8 eu fiz um loop pra printar e armazenar 3 valores em sequencia e a cada loop eu armazenava o valor em outra variavel pra somar o valor das 3 entradas e depois condicionei os valores pra dar os resultados 



   