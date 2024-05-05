def imprimir_x():
    x = 14
    print(f"X: {x}")


imprimir_x()

# Não é possível imprimir o valor de x pois
# a variável existe apenas no escopo da função
# print(f"{x}")  #  NameError: name 'x' is not defined
