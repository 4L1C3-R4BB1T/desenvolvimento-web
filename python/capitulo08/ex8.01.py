class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome} - Idade: {self.idade}")


pessoa_1 = Pessoa("Livia", 23)
pessoa_2 = Pessoa("Gabriel", 24)

pessoa_1.mostrar_dados()
pessoa_2.mostrar_dados()
