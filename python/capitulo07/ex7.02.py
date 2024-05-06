nome = input("Nome do arquivo: ")

with open(nome + ".txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print(f"\nO arquivo possui {len(linhas)} linhas")
