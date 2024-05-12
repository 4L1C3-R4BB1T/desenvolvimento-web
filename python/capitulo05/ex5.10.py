def transformar_lista(lista, funcao):
    return [funcao(n) for n in lista]


def por_extenso(n):
    numeros = [
        "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    ]
    return numeros[n]


print(transformar_lista([1, 2, 3, 4, 5], por_extenso))
