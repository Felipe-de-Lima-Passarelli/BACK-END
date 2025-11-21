caso = 1

while True:
    try:
        N1 = int(input())
        N2 = int(input())
    except EOFError:
        break

    x = str(N1)
    y = str(N2)
    sequencia = 0
    primeirox = x[0]
    tamanhox = len(x)
    tamanhoy = len(y)
    posicaofinal = 0

    try:
        for pos, i in enumerate(range (0, tamanhoy)):
            existe = True
            if y[i] == primeirox:
                for num in range(0, tamanhox):
                    if y[i + num] != x[num]:
                        existe = False
                if existe:
                    sequencia += 1
                    posicaofinal = pos + 1
    except IndexError:
        pass

    if sequencia > 0:
        print(f"Caso #{caso}:")
        print(f"Qtd.Subsequencias: {sequencia}")
        print(f"Pos: {posicaofinal}")
    else:
        print(f"Caso #{caso}:")
        print(f"Nao existe subsequencia")

    caso += 1
    print()
