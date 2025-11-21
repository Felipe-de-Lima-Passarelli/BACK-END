while True:
    try:
        N, Q = map(int, input().split())
        notas = []
        for _ in range(0, N):
            notas.append(int(input()))
        notas.sort()
        for _ in range(0, Q):
            x = int(input())
            print(notas[-x])
    except EOFError:
        break
