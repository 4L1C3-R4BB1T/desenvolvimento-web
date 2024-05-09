faixa_etaria = input("Faixa etária: ").lower()

match faixa_etaria:
    case "criança":
        print("Filme para crianças")
    case "adolescente":
        print("Filme para adolescentes")
    case "adulto":
        print("Filme para adultos")
    case _:
        print("Faixa etária inválida")
