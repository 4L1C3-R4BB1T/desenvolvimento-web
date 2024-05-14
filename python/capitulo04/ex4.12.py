frase = input("Frase: ")

cont_a = cont_o = 0

for palavra in frase.split():
    if palavra.endswith("a"):
        cont_a += 1
    elif palavra.endswith("o"):
        cont_o += 1

print(f"Palavras que terminan com A: {cont_a}")
print(f"Palavras que terminan com O: {cont_o}")
