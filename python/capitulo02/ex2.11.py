idade = int(input("Idade: "))
nacionalidade = input("Nacionalidade: ").lower()

if idade >= 16 and nacionalidade == "brasileiro" or nacionalidade == "brasileira":
    print("Pode votar")
else:
    print("Não pode votar")
