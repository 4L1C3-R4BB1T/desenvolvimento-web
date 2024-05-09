nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 6:
    print("Aprovado")
    if media == 10:
        print("Parabéns")
else:
    print("Reprovado")
