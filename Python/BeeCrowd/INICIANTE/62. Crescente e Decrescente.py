while True:
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X == Y:
        break
    else:
        if X > Y:
            print("Decrescente")
        else:
            print("Crescente")
