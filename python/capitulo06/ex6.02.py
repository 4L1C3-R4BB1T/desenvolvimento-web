frase = input("Frase: ")

lista = [palavra.replace("a", "o") for palavra in frase.split() if "a" in palavra]

print(lista)
