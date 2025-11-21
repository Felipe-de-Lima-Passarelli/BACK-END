codificador = input().split(" ")
c = 2
soma = 0

A = int(codificador[0])
N = int(codificador[1])

while N <= 0:
    for i in codificador:
        if int(codificador[c]) > 0:
            N = int(codificador[c])
        else:
            c += 1

for i in range(0, N):
    soma += A + i

print(soma)
