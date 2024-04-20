valor_inicial = float(input("Valor inicial: "))
taxa_juros = float(input("Taxa de juros mensal (%): "))
meses = int(input("Meses: "))

valor_final = valor_inicial * (1 + taxa_juros / 100) ** meses

print(f"\nValor final: R$ {valor_final:.2f}")
