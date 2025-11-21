while True:
    try:
        N, M = map(int, input().split())
        matriz = []
        for _ in range(0, N):
            linha = list(map(int, input().split()))
            while len(linha) != M:
                linha = list(map(int, input().split()))
            matriz.append(linha)

        matrizresposta = []
        for linha in range(0, N):
            linharesposta = []
            for coluna in range(0, M):
                contador = 0
                if N > 1 and M > 1:
                    if linha == 0 and coluna == 0:
                        if matriz[linha][coluna] == 0:
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                            if matriz[linha + 1][coluna] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha == 0 and coluna > 0 and coluna != (M - 1):
                        if matriz[linha][coluna] == 0:
                            if matriz[linha][coluna - 1] == 1:
                                contador += 1
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                            if matriz[linha + 1][coluna] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha > 0 and linha != (N - 1) and coluna == 0:
                        if matriz[linha][coluna] == 0:
                            if matriz[linha - 1][coluna] == 1:
                                contador += 1
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                            if matriz[linha + 1][coluna] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha > 0 and linha != (N-1) and coluna > 0 and coluna != (M - 1):
                        if matriz[linha][coluna] == 0:
                            if matriz[linha - 1][coluna] == 1:
                                contador += 1
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                            if matriz[linha + 1][coluna] == 1:
                                contador += 1
                            if matriz[linha][coluna - 1] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha == (N - 1) and coluna == 0:
                        if matriz[linha][coluna] == 0:
                            if matriz[linha - 1][coluna] == 1:
                                contador += 1
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha == (N - 1) and coluna == (M - 1):
                        if matriz[linha][coluna] == 0:
                            if matriz[linha - 1][coluna] == 1:
                                contador += 1
                            if matriz[linha][coluna - 1] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha == 0 and coluna == (M - 1):
                        if matriz[linha][coluna] == 0:
                            if matriz[linha + 1][coluna] == 1:
                                contador += 1
                            if matriz[linha][coluna - 1] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha > 0 and linha != (N - 1) and coluna == (M - 1):
                        if matriz[linha][coluna] == 0:
                            if matriz[linha - 1][coluna] == 1:
                                contador += 1
                            if matriz[linha][coluna - 1] == 1:
                                contador += 1
                            if matriz[linha + 1][coluna] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha == (N - 1) and coluna > 0 and coluna != (M - 1):
                        if matriz[linha][coluna] == 0:
                            if matriz[linha - 1][coluna] == 1:
                                contador += 1
                            if matriz[linha][coluna - 1] == 1:
                                contador += 1
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                        else:
                            contador = 9
                elif N == 1 and M == 1:
                    if linha == (N - 1) and coluna == (M - 1):
                        if matriz[linha][coluna] == 0:
                            contador += 1
                        else:
                            contador = 9
                elif N == 1 and M > 1:
                    if linha == (N - 1) and coluna == 0:
                        if matriz[linha][coluna] == 0:
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha == (N - 1) and coluna == (M - 1):
                        if matriz[linha][coluna] == 0:
                            if matriz[linha][coluna - 1] == 1:
                                contador += 1
                        else:
                            contador = 9
                elif N > 1 and M == 1:
                    if linha == 0:
                        if matriz[linha + 1][coluna] == 0:
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha > 0 and linha != (N - 1):
                        if matriz[linha + 1][coluna] == 0:
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                        if matriz[linha - 1][coluna] == 0:
                            if matriz[linha][coluna + 1] == 1:
                                contador += 1
                        else:
                            contador = 9
                    elif linha == (N - 1):
                        if matriz[linha + 1][coluna] == 0:
                            if matriz[linha - 1][coluna] == 1:
                                contador += 1
                        else:
                            contador = 9

                linharesposta.append(contador)
            matrizresposta.append(linharesposta)
        for linha in matrizresposta:
            for num in linha:
                print(num, end = "")
            print()

    except EOFError:
        break
