qtd = 0
soma = 0

while (numero := float(input("Digite um número: "))) >= 0:
    soma += numero
    qtd += 1

media = soma / qtd

print(f"Média: {media:.2f}")
