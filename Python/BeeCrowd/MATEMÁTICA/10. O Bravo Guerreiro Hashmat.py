while True:
    try:
        Soldados_Hashmat, Soldados_Inimigos = map(int, input().split())

        print(abs(Soldados_Hashmat - Soldados_Inimigos))

    except EOFError:
        break
