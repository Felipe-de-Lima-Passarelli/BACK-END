N = int(input())
while N < 0 or N > 1000000:
    N = int(input())

contagem100 = 0
contagem50 = 0
contagem20 = 0
contagem10 = 0
contagem5 = 0
contagem2 = 0
contagem1 = 0
print(N)

while N >= 100:
    contagem100 += 1
    N = N - 100

while N >= 50:
    contagem50 += 1
    N = N - 50

while N >= 20:
    contagem20 += 1
    N = N - 20

while N >= 10:
    contagem10 += 1
    N = N - 10

while N >= 5:
    contagem5 += 1
    N = N - 5

while N >= 2:
    contagem2 += 1
    N = N - 2

while N == 1:
    contagem1 += 1
    N = N - 1

print(f"{contagem100} nota(s) de R$ 100,00")
print(f"{contagem50} nota(s) de R$ 50,00")
print(f"{contagem20} nota(s) de R$ 20,00")
print(f"{contagem10} nota(s) de R$ 10,00")
print(f"{contagem5} nota(s) de R$ 5,00")
print(f"{contagem2} nota(s) de R$ 2,00")
print(f"{contagem1} nota(s) de R$ 1,00")
