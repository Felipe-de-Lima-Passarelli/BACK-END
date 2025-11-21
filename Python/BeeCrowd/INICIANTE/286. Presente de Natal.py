while True:
    N = int(input())
    if N == 0:
        break
    xi = list(map(int, input().split()))

    if N == 1:
        print(sum(xi), sum(xi))
    else:
        valores = []
        for i in range(0, N):
            valores.append(xi[i] + xi[-1 - i])
        valores.sort(reverse = True)

        print(valores[0], valores[-1])
