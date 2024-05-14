class Veiculo:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        if valor <= self.velocidade:
            self.velocidade -= valor
        else:
            self.velocidade = 0

    def exibir_velocidade(self):
        print(f"Velocidade: {self.velocidade}")


class Carro(Veiculo):
    def __init__(self, marca):
        super().__init__()
        self.marca = marca


carro = Carro("Gol")

carro.acelerar(10)
carro.exibir_velocidade()
carro.frear(2)
carro.exibir_velocidade()
carro.frear(50)
carro.exibir_velocidade()
