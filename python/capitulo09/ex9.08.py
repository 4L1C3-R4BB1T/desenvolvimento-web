palavra_secreta = "batata"

try:
    while True:
        palavra = input("Adivinhe a palavra secreta: ")
        if not palavra.isalpha():
            raise ValueError("Entrada inválida")
        if palavra == palavra_secreta:
            print("Você acertou")
            break
except ValueError as error:
    print(error)
