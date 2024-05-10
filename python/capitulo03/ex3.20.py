n = int(input("N: "))

for i in range(1, n + 1):
    fatorial = 1
    for j in range(2, i + 1):
        fatorial *= j
    print(f"Fatorial ({i}): {fatorial}")
