a = float(input("Número A: "))
b = float(input("Número B: "))
op = input("Operação: ")

match op:
    case "+":
        print(f"Soma: {a + b}")
    case "-":
        print(f"Subtração: {a - b}")
    case "/":
        print(f"Divisão: {a / b}")
    case "*":
        print(f"Multiplicação: {a * b}")
    case _:
        print("Operação inválida")
