nome = input("Nome do arquivo: ")

with open(nome + ".txt", "r", encoding="utf-8") as arquivo:
    linha = arquivo.read()
    print(linha)
