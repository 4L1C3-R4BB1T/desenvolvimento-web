numeros = []

for i in range(5):
    numero = int(input(f"Digite o numero #{i + 1}: "))
    numeros.append(numero)

impar = False

for numero in numeros:
    if numero % 2 != 0:
        impar = True
        break

if impar:
    print("Há pelo menos um número ímpar")
else:
    print("Todos os números são pares")
