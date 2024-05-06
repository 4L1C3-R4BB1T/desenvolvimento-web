class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("Som do animal...")


animal = Animal("Manga", 2)

animal.emitir_som()
