i = 1
while True:
    X1, Y1, X2, Y2 = map(int, input().split())
    if X1 == Y1 == X2 == Y2 == 0:
        break

    plano_Y_fazenda = [Y1, Y2]
    plano_X_fazenda = [X1, X2]

    N = int(input())
    contador = 0
    for _ in range(0, N):
        X, Y = map(int, input().split())
        if X2 >= X >= X1:
            if Y2 <= Y <= Y1:
                contador += 1

    print(f"Teste {i}")
    print(contador)
    i += 1
