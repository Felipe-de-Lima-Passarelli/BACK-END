N = int(input())

for i in range(0, N):
    soma = 0
    X, Y = input().split()
    X = int(X)
    Y = int(Y)

    if X%2 == 0:
        X += 1
        for num in range(0, Y):
            soma += X
            X += 2
        print(soma)
    else:
        for num in range(0, Y):
            soma += X
            X += 2
        print(soma)
