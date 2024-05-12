def contagem_regressiva(n: int):
    print(n, end=", ")
    if n > 0:
        contagem_regressiva(n - 1)
    else:
        print("Contagem regressiva finalizada!")


contagem_regressiva(10)
