def calculadora(op: int, a: float, b: float) -> float:
    try:
        if op == 1:
            return a + b
        elif op == 2:
            return a - b
        elif op == 3:
            return a / b
        elif op == 4:
            return a * b
        else:
            raise ValueError("Entrada inválida")
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    except TypeError:
        print("A entrada deve conter apenas números")


# 1. Soma
# 2. Subtração
# 3. Divisão
# 4. Multiplicação

print(calculadora(1, 2, 3))
print(calculadora("s", 2, 3))
print(calculadora(1, "d", 3))
print(calculadora(3, 2, 0))
