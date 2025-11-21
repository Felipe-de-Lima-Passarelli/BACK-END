from math import ceil

V, N = map(int, input().split())
respostas = []

inicio = 10

while inicio < 100:
    respostas.append(ceil(((V*N) * inicio)/100))
    inicio += 10

print(*respostas)
