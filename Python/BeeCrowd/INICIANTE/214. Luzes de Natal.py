N = int(input())
for _ in range(0, N):
    X = bin(int(input()))
    X = X[2:]

    contador = 0
    maior = 0

    for numeros in X:
        if numeros == "1":
            contador += 1
            if contador > maior:
                maior = contador
        else:
            contador = 0

    print(maior)
