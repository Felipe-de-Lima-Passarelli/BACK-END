N = int(input())

for _ in range(0, N):
    maria = 0
    joao = 0
    for _ in range(0, 3):
        X, D = map(int, input().split())
        joao += X * D
    for _ in range(0, 3):
        X, D = map(int, input().split())
        maria += X * D

    if joao > maria:
        print("JOAO")
    else:
        print("MARIA")
