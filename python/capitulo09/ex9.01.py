try:
    numero_1 = int(input("Número 1: "))
    numero_2 = int(input("Número 2: "))
    divisao = numero_1 / numero_2
    print(f"{divisao}")
except ZeroDivisionError:
    print("Não é possível dividir por 0")
except ValueError:
    print("Entrada inválida")
