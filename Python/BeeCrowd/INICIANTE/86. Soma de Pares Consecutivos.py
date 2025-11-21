while True:
    soma = 0
    X = int(input())
    if X == 0:
        break

    if X%2 == 0:
        for i in range(0, 5):
            soma += X
            X += 2
        print(soma)
    else:
        X += 1
        for i in range(0, 5):
            soma += X
            X += 2
        print(soma)
