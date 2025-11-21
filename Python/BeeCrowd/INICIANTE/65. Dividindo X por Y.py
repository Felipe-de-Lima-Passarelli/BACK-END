N = int(input())

for i in range(0, N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    try:
        print(f"{X/Y}")
    except ZeroDivisionError:
        print("divisao impossivel")
