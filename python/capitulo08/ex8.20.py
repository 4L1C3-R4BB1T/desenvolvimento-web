class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def mostrar_dados(self):
        print(f"{self.numerador}/{self.denominador}")

    def multiplicar(self, fracao):
        resultado_numerador = self.numerador * fracao.numerador
        resultado_denominador = self.denominador * fracao.denominador
        return Fracao(resultado_numerador, resultado_denominador)


fracao_1 = Fracao(1, 2)
fracao_2 = Fracao(3, 4)

fracao_1.mostrar_dados()
fracao_2.mostrar_dados()
fracao_1.multiplicar(fracao_2).mostrar_dados()
