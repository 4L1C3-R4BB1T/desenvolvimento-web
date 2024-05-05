from math import radians, sin, cos, tan

angulo = float(input("Ângulo: "))

radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f"\nSeno de {angulo}º: {seno:.2f}")
print(f"Cosseno de {angulo}º: {cosseno:.2f}")
print(f"Tangente de {angulo}º: {tangente:.2f}")
