while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    matriz = []
    tamanho_max = 0

    for _ in range(N):
        linhas = list(map(int, input().split()))
        matriz.append(linhas)

    for i in range(N):
        for j in range(M):
            for k in range(i, N):
                for l in range(j, M):
                    subsequencia = []
                    for x in range(i, k + 1):
                        subsequencia.extend(matriz[x][j:l + 1])

                    crescente = True
                    for idx in range(1, len(subsequencia)):
                        if subsequencia[idx] <= subsequencia[idx - 1]:
                            crescente = False
                            break

                    if crescente:
                        tamanho_max = max(tamanho_max, len(subsequencia))

    print(tamanho_max)
