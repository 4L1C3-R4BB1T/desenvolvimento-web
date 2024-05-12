def decifrar_mensagem(mensagem: str):
    if len(mensagem) > 0:
        letra = chr((ord(mensagem[0]) - 98) % 26 + 97)
        return letra + decifrar_mensagem(mensagem[1:])
    return mensagem


print(decifrar_mensagem("mjwjb"))
