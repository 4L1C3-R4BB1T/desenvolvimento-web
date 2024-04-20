import math 

altitude_inicial = float(input("Altitude inicial: "))

gravidade = 10
tempo = math.sqrt(2 * altitude_inicial / gravidade)

print(f"\nTempo: {tempo:.2f}")
