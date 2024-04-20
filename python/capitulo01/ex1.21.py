distancia = float(input("Distância percorrida: "))
tempo = float(input("Tempo gasto: "))
aceleracao = float(input("Aceleração: "))

velocidade_inicial = (distancia / tempo) - (aceleracao * tempo / 2) 
velocidade_final = velocidade_inicial + aceleracao * tempo

print(f"\nVelocidade inicial: {velocidade_inicial:.2f}")
print(f"Velocidade final: {velocidade_final:.2f}")
