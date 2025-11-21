X, Y = input().split()
X = int(X)
Y = int(Y)
c = 1

while X <= 1 or X >= 20 or Y < X or Y >= 100000:
    X, Y = input().split()
    X = int(X)
    Y = int(Y)

while True:
    for i in range(0, X):
        if c >= Y:
            print(c)
            break
        if i == (X - 1):
            print(f"{c}")
            c += 1
        else:
            print(f"{c}", end = " ")
            c += 1
    if c >= Y:
        break
