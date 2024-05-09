emocao = input("Emoção: ")

match emocao:
    case "feliz":
        print(":)")
    case "triste":
        print(":(")
    case "nervoso":
        print(":s")
    case "furioso":
        print(">:(")
    case "calmo":
        print("B)")
    case _:
        print("Emoção inválida")
