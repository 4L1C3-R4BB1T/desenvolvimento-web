ano = int(input("Ano: "))

if ano % 4 == 0:
    if ano % 100 != 0:
        print("\nÉ bissexto")
    else:
        print("\nNão é bissexto")
else:
    if ano % 400 == 0:
        print("\nÉ bissexto")
    else:
        print("\nNão é bissexto")
