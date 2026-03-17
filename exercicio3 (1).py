groceries_list = ["pasta", "coffe", "fruit", "sauce", "fish"]  #defini uma lista

for item in groceries_list: #printar itens
    print([item])

how_many = len(groceries_list) # Tamanho lista
print(f"There are {how_many} items in the list")

item_coffe = ("coffe" in groceries_list) # Retorna TRue se tiver cafe na lista
if (item_coffe == True):
    print("Coffe is in the list")
else:
    print("There are no coffe in the list")


new_item = input("Add other item on the list: \n") # Adiciona novo item 
groceries_list.append(new_item)

print("The list after the addition: \n")
print(groceries_list)
