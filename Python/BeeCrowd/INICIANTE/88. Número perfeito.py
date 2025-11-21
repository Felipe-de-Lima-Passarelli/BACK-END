N = int(input())
while N < 1 or N > 20:
    N = int(input())

for i in range(N):
    soma = 0
    X = int(input())
    while X < 1 or X > 100000000:
        X = int(input())

    for num in range(1, X):
        if X%num == 0:
            soma += num

    if soma == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
