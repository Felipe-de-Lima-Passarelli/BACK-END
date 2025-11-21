while True:
    try:
        N = int(input())
    except EOFError:
        break

    while N < 3 or N > 70:
        N = int(input())

    matriz = []

    for i in range(0, N):
        linha = [0] * N
        matriz.append(linha)

    valor = 1
    for camada in range((N + 1) // 2):
        for i in range(camada, N - camada):
            if i == camada:
                matriz[camada][i] = 1
                matriz[N - camada - 1][i] = 2
                matriz[i][camada] = 1
                matriz[i][N - camada - 1] = 2
            elif i == ((N - camada) - 1):
                matriz[camada][i] = 2
                matriz[N - camada - 1][i] = 1
                matriz[i][camada] = 2
                matriz[i][N - camada - 1] = 1
            else:
                matriz[camada][i] = 3
                matriz[N - camada - 1][i] = 3
                matriz[i][camada] = 3
                matriz[i][N - camada - 1] = 3

    for linha in matriz:
        for num in linha:
            print(num, end = "")
        print()
