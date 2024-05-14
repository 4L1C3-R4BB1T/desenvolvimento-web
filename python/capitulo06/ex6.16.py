lista = [1, 2, 3, 4, 5, 6]

indices = [lista[i] for i in range(0, len(lista), 2)]
indices.reverse()

for i in range(0, len(lista), 2):
    lista[i] = indices.pop(0)

print(lista)
