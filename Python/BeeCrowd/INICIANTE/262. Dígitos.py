while True:
    try:
        C = int(input())
        for _ in range(0, C):
            N, M = map(int, input().split())
            X = str(N**M)
            print(len(X))

    except EOFError:
        break
