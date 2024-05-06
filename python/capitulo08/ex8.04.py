class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, segundos):
        self.velocidade += 10 * segundos

    def frear(self, segundos):
        self.velocidade -= 5 * segundos


carro = Carro()

carro.acelerar(10)
print(f"Velocidade: {carro.velocidade}")

carro.frear(2)
print(f"Velocidade: {carro.velocidade}")
