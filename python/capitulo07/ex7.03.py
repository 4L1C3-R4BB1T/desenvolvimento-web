nome = input("Nome do arquivo: ")

with open(nome + ".txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

inversao = [l[::-1] for l in linhas]

with open(nome + "_invertido.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(inversao)
