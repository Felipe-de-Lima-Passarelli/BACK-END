while True:
    try:
        N = int(input())

        if N == 1:
            print(0)
        else:
            contador = 0
            while N >= 2:
                N /= 2
                contador += 1

            print(contador)

    except EOFError:
        break
