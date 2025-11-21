while True:
    try:
        H, M = map(int, input().split())
        QT = int((H*60)/M)
        dados = list(map(float, input().split()))
        Xmedia = sum(dados)/len(dados)
        X = 0

        for numeros in dados:
            X += ((numeros - Xmedia)**2)
        resposta = X/(QT - 1)
        print(f"{resposta**(1/2):.5f}")

    except EOFError:
        break
