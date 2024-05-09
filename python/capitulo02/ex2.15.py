palavra = input("Palavra: ").lower()

vogais = "aeiou"

if palavra[0] in vogais:
    print("Começa com vogal")
else:
    print("Começa com consoante")
