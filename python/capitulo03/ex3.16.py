numeros = []

for i in range(10):
    numero = float(input(f"Número {i + 1}: "))
    numeros.append(numero)

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor < numero

print(f"\nMaior: {maior}\nMenor: {menor}")
