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

    for camada in range((N + 1) // 2):
        valor = camada + 1
        for i in range(camada, N - camada):
            matriz[camada][i] = valor
            matriz[N - camada - 1][i] = valor
            matriz[i][camada] = valor
            matriz[i][N - camada - 1] = valor

    for linha in matriz:
        print(" ".join(f"{elemento:>3}" for elemento in linha))

    print()
