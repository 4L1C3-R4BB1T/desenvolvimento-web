from collections import Counter

frase = input("Frase: ")

contador = Counter(frase.split())

for palavra, vezes in contador.items():
    print(f'"{palavra}" aparece {vezes} vez(es)')
