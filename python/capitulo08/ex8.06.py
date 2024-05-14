from math import pi


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return self.raio * self.raio * pi


circulo = Circulo(5)

print(f"Área: {circulo.area():.2f}")
