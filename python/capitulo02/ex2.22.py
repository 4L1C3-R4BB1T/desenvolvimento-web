clima = input("Clima: ").lower()

match clima:
    case "ensolarado":
        print("Óculos de sol")
    case "chuvoso":
        print("Guarda-chuva")
    case "nublado":
        print("Casaco")
    case _:
        print("Clima inválido")
