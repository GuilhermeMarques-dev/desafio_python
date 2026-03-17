funcionario = {
        "nome": "Maria",
        "cargo": "Analista",
        "salario": 4000
    }

# printando formatado 
def printar_funcionario(funcionario):
 print("Funcionário: ")
 print(f"{funcionario["nome"]}")
 print(f"{funcionario["cargo"]}")
 print(f"R${funcionario["salario"]}")
# 10% a mais de salario

def aumentar_salario(salario):
    salario_aumentado =  (salario * 1.10)
    print(f"Salario dps do reajuste: R$ {salario_aumentado}")
    return salario_aumentado



printar_funcionario(funcionario)
funcionario["salario"] = aumentar_salario(funcionario["salario"])
printar_funcionario(funcionario)

