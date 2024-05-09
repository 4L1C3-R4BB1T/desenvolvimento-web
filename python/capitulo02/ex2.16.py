peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Você está abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Você está com o peso normal")
elif 25 <= imc <= 29.9:
    print("Você está com sobrepeso")
else:
    print("Você está com obesidade")
