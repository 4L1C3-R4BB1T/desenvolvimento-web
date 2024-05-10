numeros = []

for i in range(10):
    numero = float(input(f"Número {i + 1}: "))
    numeros.append(numero)

maior = segundo_maior = float("-inf")
menor = segundo_menor = float("inf")

for numero in numeros:
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero < maior and numero > segundo_maior:
        segundo_maior = numero

    if numero < menor:
        segundo_menor = menor
        menor = numero
    elif numero > menor and numero < segundo_menor:
        segundo_menor = numero

print(f"\nSegundo maior: {segundo_maior}\nSegundo menor: {segundo_menor}")
