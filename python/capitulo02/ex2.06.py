texto = input("Texto: ")

texto = texto.replace(" ", "").lower()

if texto == texto[::-1]:
    print("É palíndromo")
else:
    print("Nao é palíndromo")
