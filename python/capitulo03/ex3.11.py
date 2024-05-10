from math import sqrt

for i in range(1, 101):
    raiz = sqrt(i)

    if raiz == int(raiz):
        print(i, end=", ")
