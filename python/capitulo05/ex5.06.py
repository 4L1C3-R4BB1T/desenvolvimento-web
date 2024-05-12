from typing import List

idades = [11, 12, 13, 14, 15]

idade = int(input("Idade para adicionar: "))


def adicionar(lista: List, idade: int):
    lista.append(idade)


adicionar(idades, idade)
print(idades)
