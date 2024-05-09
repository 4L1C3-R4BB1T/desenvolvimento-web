cor = input("Cor: ").lower()

match cor:
    case "verde":
        print("Prossiga")
    case "amarelo":
        print("Prepare-se para frear")
    case "vermelho":
        print("Pare")
    case _:
        print("Cor inválida")
