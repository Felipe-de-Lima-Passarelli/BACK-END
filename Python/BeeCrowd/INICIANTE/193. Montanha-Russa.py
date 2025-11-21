while True:
    try:
        N, Amin, Amax = map(int, input().split())
        contador = 0

        for _ in range(0, N):
            A = int(input())
            if Amin <= A <= Amax:
                contador += 1

        print(contador)

    except EOFError:
        break
