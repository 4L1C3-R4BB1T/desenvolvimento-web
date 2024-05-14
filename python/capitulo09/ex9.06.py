from random import randint

aleatorio = randint(1, 10)

while True:
    try:
        numero = int(input("Número (1 a 10): "))
        if numero == aleatorio:
            print("Você acertou")
            break
        else:
            print("Você errou")
    except ValueError:
        print("Entrada inválida")
