idade = int(input("Idade: "))
genero = input("Gênero: ").lower()

if (genero == "f" and idade >= 60) or (genero == "m" and idade >= 65):
    print("Pode aposentar")
else:
    print("Não pode aposentar")
