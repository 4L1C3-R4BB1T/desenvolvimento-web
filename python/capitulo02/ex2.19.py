from random import randint

aleatorio = randint(1, 10)

numero = int(input("Número (1 a 10): "))

if numero == aleatorio:
    print("Você acertou")
elif numero < aleatorio:
    print("O número é maior")
else:
    print("O número é menor")
