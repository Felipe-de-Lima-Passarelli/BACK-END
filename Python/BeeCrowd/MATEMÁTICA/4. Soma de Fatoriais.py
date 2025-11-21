while True:
    try:
        M, N = map(int, input().split())

        def fatorial(x):
            if x <= 1:
                return 1
            else:
                return x * fatorial(x - 1)

        print(fatorial(M) + fatorial(N))
    except EOFError:
        break
