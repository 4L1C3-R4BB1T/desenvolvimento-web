nome = input("Nome: ")
salario = float(input("Salário: "))
imposto = float(input("Imposto (%): "))

salario_liquido = salario * (1 - imposto / 100)

print(f"\n{nome} tem um salário líquido de R$ {salario_liquido:.2f}.") 
