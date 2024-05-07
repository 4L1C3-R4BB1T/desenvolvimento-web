from typing import List


def avg(nums: List) -> float:
    try:
        return sum(nums) / len(nums)
    except ZeroDivisionError:
        print("A lista está vazia")
    except TypeError:
        print("A lista deve conter apenas números")


lista_1 = [1, 2, 3, 4, 5]
lista_2 = [1, "g", 3, 4, 5]
lista_3 = []

print(avg(lista_1))
print(avg(lista_2))
print(avg(lista_3))
