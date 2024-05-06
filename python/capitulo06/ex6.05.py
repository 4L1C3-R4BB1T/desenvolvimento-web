alunos = {}

num = int(input("Número de alunos: "))

for i in range(num):
    nome = input("\nNome: ")
    nota = float(input("Nota: "))
    alunos[nome] = nota

dicionario = {nome: nota for nome, nota in alunos.items() if nota >= 7}

print(f"\n{dicionario}")
