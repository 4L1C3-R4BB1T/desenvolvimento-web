class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


retangulo = Retangulo(14.6, 3)

print(f"Área: {retangulo.area():.2f}")
