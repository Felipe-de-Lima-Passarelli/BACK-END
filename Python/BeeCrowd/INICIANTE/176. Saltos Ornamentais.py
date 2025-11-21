N = int(input())
while N < 0 or N > 100:
    N = int(input())

for i in range(0, N):
    nome = str(input())
    GD = float(input())
    while GD < 1.2 or GD > 3.8:
        GD = float(input())

    N1, N2, N3, N4, N5, N6, N7 = map(float, input().split())
    notas = [N1, N2, N3, N4, N5, N6, N7]
    notas.sort()
    notas.pop(0)
    notas.pop()
    soma = sum(notas)
    notafinal = soma * GD
    print(f"{nome} {notafinal:.2f}")
