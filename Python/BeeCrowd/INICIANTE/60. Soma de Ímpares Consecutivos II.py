N = int(input())

for i in range(0, N):
    somaimpar = 0
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X > Y:
        for num in range(Y + 1, X):
            if num%2 != 0:
                somaimpar += num
        print(somaimpar)
    else:
        for num in range(X + 1, Y):
            if num%2 != 0:
                somaimpar += num
        print(somaimpar)
