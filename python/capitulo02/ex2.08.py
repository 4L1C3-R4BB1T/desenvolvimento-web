data = input("Data: ")

if len(data) == 10 and data[2] == "/" and data[5] == "/":
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])
    if (1 <= dia <= 31) and (1 <= mes <= 12) and (1 <= ano <= 9999):
        print("Data válida")
    else:
        print("Data inválida")
else:
    print("Data inválida")
