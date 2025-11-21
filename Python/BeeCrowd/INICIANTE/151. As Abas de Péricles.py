N, M = map(int, input().split())
while N <= 0 or N >= 500 or M <= 0 or M >= 500:
    N, M = map(int, input().split())

abertas = N

for i in range(0, M):
    escolha = str(input())
    while escolha != "fechou" and escolha != "clicou":
        escolha = str(input())

    if escolha == "fechou":
        abertas += 1
    else:
        abertas -= 1

print(abertas)
