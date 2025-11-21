while True:
    T = int(input())
    if T == 0:
        break

    while T < 1 or T > 100:
        T = int(input())

    for i in range(0, T):
        N = int(input())
        while N < 3 or N > 10000:
            N = int(input())

        if N%2 == 0:
            pedidos = 2 + ((N - 2) * 2)
        else:
            pedidos = 1 + ((N - 1) * 2)

        print(pedidos)
