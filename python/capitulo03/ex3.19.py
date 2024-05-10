palavra = input("Palavra: ").lower()

invertida = ""

for i in range(len(palavra) - 1, -1, -1):
    invertida += palavra[i]

if palavra == invertida:
    print("É palíndromo")
else:
    print("Nao é palíndromo")
