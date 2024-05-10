palavra = input("Palavra: ").lower()

invertida = ""

for i in range(len(palavra) - 1, -1, -1):
    invertida += palavra[i]

if palavra == invertida:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
