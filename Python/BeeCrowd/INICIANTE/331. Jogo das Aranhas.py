N = int(input())

for K in range(1, 10**16):
    circulo = [1] * N + [2] * N

    indice = 0
    eliminadas = 0

    while eliminadas < N:
        indice = (indice + K - 1) % len(circulo)
        if circulo[indice] == 1:
            break
        del circulo[indice]
        eliminadas += 1

    if eliminadas == N:
        print(K)
        break
