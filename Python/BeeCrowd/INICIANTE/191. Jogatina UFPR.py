while True:
    try:
        N, I = map(int, input().split())

        contador = 0
        for _ in range(0, N):
            i, j = map(int, input().split())
            if i == I and j == 0:
                contador +=1

        print(contador)

    except EOFError:
        break
