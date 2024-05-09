temperatura = float(input("Temperatura: "))

if temperatura < 36:
    print("Temperatura abaixo da faixa normal")
elif temperatura > 37:
    print("Temperatura acima da faixa normal")
else:
    print("Temperatura dentro da faixa normal")
