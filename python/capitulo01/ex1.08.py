import math

angulo = float(input("Ângulo (0º ~ 360º): "))

radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f"\nSeno de {angulo}º: {seno:.2f}")
print(f"Cosseno de {angulo}º: {cosseno:.2f}")
print(f"Tangente de {angulo}º: {tangente:.2f}")
