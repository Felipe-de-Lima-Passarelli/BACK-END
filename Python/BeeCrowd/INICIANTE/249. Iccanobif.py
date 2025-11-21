N = int(input())
x1 = 1
x2 = 1
respostas = []

if N == 1:
    print(1)
elif N == 2:
    print(1, 1)
else:
    for i in range(0, (N - 2)):
        respostas.append(x1 + x2)
        x1, x2 = x2, x1+x2
    respostas.reverse()
    print(*respostas, end = "")
    print(f" {1} {1}")
