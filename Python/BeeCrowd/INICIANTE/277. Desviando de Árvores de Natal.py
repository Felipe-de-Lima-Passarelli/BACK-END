while True:
    M = int(input())
    if M == 0:
        break
    matriz = []
    local = 1
    desviadas = 0
    for _ in range(0, M):
        L, C, R = map(int, input().split())
        matriz.append(([L, C, R]))

    for i in range(0, M):
        if matriz[i][local] == 1:
            if local == 1:
                desviadas += 1
                if matriz[i][local - 1] == 0:
                    local = 0
                else:
                    local = 2
            elif local == 0:
                if matriz[i][local + 1] == 0:
                    desviadas += 1
                    local = 1
                else:
                    desviadas += 2
                    local = 2
            else:
                if matriz[i][local - 1] == 0:
                    desviadas += 1
                    local = 1
                else:
                    desviadas += 2
                    local = 0

    print(desviadas)
