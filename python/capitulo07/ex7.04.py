import os

nome = input("Nome do arquivo: ")

os.rename(nome + ".txt", nome + "_renomeado.txt")
