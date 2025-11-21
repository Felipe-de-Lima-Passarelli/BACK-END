X = int(input())
Y = int(input())
somaimpares = 0

if X > Y:
    for i in range(Y+1, X):
        if i%2 != 0:
            somaimpares += i
else:
    for i in range(X+1, Y):
        if i%2 != 0:
            somaimpares += i

print(somaimpares)
