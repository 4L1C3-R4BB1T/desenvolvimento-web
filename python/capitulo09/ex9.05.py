def read(nome: str):
    try:
        with open(nome, encoding="utf-8") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except IOError:
        print("Não foi possível ler o arquivo")


read("teste.txt")
read("teste2.txt")
