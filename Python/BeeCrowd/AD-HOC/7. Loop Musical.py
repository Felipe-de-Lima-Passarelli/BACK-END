while True:
    N = int(input())
    if N == 0:
        break

    dados = list(map(int, input().split()))
    loop = []
    for numeros in dados:
        loop.append(numeros)
    loop.append(loop[0])

    picos = 0
    for i in range(0, (len(loop) - 1)):
        if i == 0:
            if (loop[i] > loop[i + 1] and loop[i] > loop[-2]) or (loop[i] < loop[i + 1] and loop[i] < loop[-2]):
                picos += 1
        else:
            if (loop[i] > loop[i + 1] and loop[i] > loop[i - 1]) or (loop[i] < loop[i + 1] and loop[i] < loop[i - 1]):
                picos += 1

    print(picos)
