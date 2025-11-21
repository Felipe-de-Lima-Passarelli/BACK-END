while True:
    N = int(input())
    while N < 0 or N > 100:
        N = int(input())

    if N == 0:
        break

    matriz = []

    for i in range(0, N):
        linha = [0] * N
        matriz.append(linha)

    valor = 1
    for camada in range((N + 1) // 2):
        for i in range(camada, N - camada):
            matriz[camada][i] = valor + i
            matriz[N - camada - 1][(N - 1) - i] = valor + i
            matriz[i][camada] = valor + i
            matriz[(N - 1) - i][N - camada - 1] = valor + i
        valor -= 1

    for linha in matriz:
        print(" ".join(f"{elemento:>3}" for elemento in linha))

    print()
