while True:
    B, N = map(int, input().split())
    if not (B or N):
        break

    reserva_monetaria = list(map(int, input().split()))
    bancos = []

    for _ in range(0, N):
        D, C, V = map(int, input().split())
        bancos.append([D, C, V, 0])

    for i in range(1, (len(reserva_monetaria) + 1)):
        bancos[i - 1][3] = reserva_monetaria[bancos[i - 1][0] - 1]

    for testes in bancos:
        bancos[testes[1] - 1][3] += testes[2]
        testes[3] -= testes[2]

    resposta_final = "S"

    for testes in bancos:
        if testes[3] < 0:
            resposta_final = "N"
            break

    print(resposta_final)
