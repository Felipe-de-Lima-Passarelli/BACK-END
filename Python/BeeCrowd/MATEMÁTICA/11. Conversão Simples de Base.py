while True:
    numero = input()

    if numero[0] == "-":
        break

    if numero[:2] == "0x" or numero[:2] == "0X":
        print(int(numero, 16))
    else:
        print(hex(int(numero)))
