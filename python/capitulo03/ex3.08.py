numero = int(input("Número: "))

fatorial = 1

for i in range(2, numero + 1):
    fatorial *= i

print(f"Fatorial: {fatorial}")
