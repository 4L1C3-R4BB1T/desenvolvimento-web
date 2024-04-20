nome = input("Nome: ")
preco_custo = float(input("Preço de custo: "))
preco_venda = float(input("Preço de venda: "))
estoque = int(input("Quantidade em estoque: "))

lucro = (preco_venda - preco_custo) * estoque

print(f"\nLucro: R$ {lucro:.2f}")
