while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    troco = M - N
    contagem = 0

    while troco >= 100:
        troco -= 100
        contagem += 1
    while troco >= 50:
        troco -= 50
        contagem += 1
    while troco >= 20:
        troco -= 20
        contagem += 1
    while troco >= 10:
        troco -= 10
        contagem += 1
    while troco >= 5:
        troco -= 5
        contagem += 1
    while troco >= 2:
        troco -= 2
        contagem += 1

    if troco == 0 and contagem == 2:
        print("possible")
    else:
        print("impossible")
