X = int(input())
while X < 1 or X > 1000:
    X = int(input())

if X%2 != 0:
    for i in range(X, X+11):
        if i%2 != 0:
            print(i)
else:
    for i in range(X, X+12):
        if i%2 != 0:
            print(i)
