while True:
    try:
        N = int(input())
    except EOFError:
        break

    while N < 5 or N > 101 or N%2 == 0:
        N = int(input())

    matriz = []

    for i in range(0, N):
        linha = [0] * N
        matriz.append(linha)

    for i in range(N):
        matriz[i][i] = 2
        matriz[i][N - i - 1] = 3

    inicio = N // 3
    fim = N - inicio
    for i in range(inicio, fim):
        for j in range(inicio, fim):
            matriz[i][j] = 1

    centro = N // 2
    matriz[centro][centro] = 4

    for linha in matriz:
        for num in linha:
            print(num, end = "")
        print()
    print()
