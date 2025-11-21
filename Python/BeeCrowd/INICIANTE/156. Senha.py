while True:
    try:
        N = int(input())
        while N < 1001 or N > 9999:
            N = int(input())
    except EOFError:
        break

    print(N - 1)
