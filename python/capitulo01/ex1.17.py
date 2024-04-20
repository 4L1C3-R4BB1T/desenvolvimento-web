velocidade_inicial = float(input("Velocidade inicial: "))
velocidade_final = float(input("Velocidade final: "))
tempo_transicao = float(input("Tempo de transição: "))

aceleracao = (velocidade_final - velocidade_inicial) / tempo_transicao

print(f"\nAceleração: {aceleracao:.2f}")
