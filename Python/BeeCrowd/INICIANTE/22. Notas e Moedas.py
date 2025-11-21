N = float(input())
while N < 0 or N > 1000000:
    N = float(input())

N = N*100
#Notas -> 100, 50, 20, 10, 5 e 2
contagem100 = 0
contagem50 = 0
contagem20 = 0
contagem10 = 0
contagem5 = 0
contagem2 = 0

#Moedas -> 1, 0.50, 0.25, 0.10, 0.05 e 0.01
contagem1 = 0
contagem050 = 0
contagem025 = 0
contagem010 = 0
contagem005 = 0
contagem001 = 0

while N >= 10000:
    contagem100 += 1
    N = N - 10000

while N >= 5000:
    contagem50 += 1
    N = N - 5000

while N >= 2000:
    contagem20 += 1
    N = N - 2000

while N >= 1000:
    contagem10 += 1
    N = N - 1000

while N >= 500:
    contagem5 += 1
    N = N - 500

while N >= 200:
    contagem2 += 1
    N = N - 200

while N >= 100:
    contagem1 += 1
    N = N - 100

while N >= 50:
    contagem050 += 1
    N = N - 50

while N >= 25:
    contagem025 += 1
    N = N - 25

while N >= 10:
    contagem010 += 1
    N = N - 10

while N >= 5:
    contagem005 += 1
    N = N - 5

while N >= 1:
    contagem001 += 1
    N = N - 1

print("NOTAS:")
print(f"{contagem100} nota(s) de R$ 100.00")
print(f"{contagem50} nota(s) de R$ 50.00")
print(f"{contagem20} nota(s) de R$ 20.00")
print(f"{contagem10} nota(s) de R$ 10.00")
print(f"{contagem5} nota(s) de R$ 5.00")
print(f"{contagem2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{contagem1} moeda(s) de R$ 1.00")
print(f"{contagem050} moeda(s) de R$ 0.50")
print(f"{contagem025} moeda(s) de R$ 0.25")
print(f"{contagem010} moeda(s) de R$ 0.10")
print(f"{contagem005} moeda(s) de R$ 0.05")
print(f"{contagem001} moeda(s) de R$ 0.01")
