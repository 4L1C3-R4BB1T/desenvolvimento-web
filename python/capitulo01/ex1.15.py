valor_total = float(input("Valor total da venda: "))
percentual_desconto = float(input("Percentual de desconto: "))
percentual_imposto = float(input("Percentual de imposto: "))

valor_desconto = valor_total * (1 - percentual_desconto / 100)
valor_final = valor_desconto * (1 - percentual_imposto / 100)

print(f"\nPreço final: R$ {valor_final:.2f}")
