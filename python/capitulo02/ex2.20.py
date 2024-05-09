cpf = input("CPF: ")

if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido")
else:
    print("CPF inválido")
