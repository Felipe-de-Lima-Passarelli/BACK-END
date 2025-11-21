N = int(input())
while N < 0 or N > 100:
    N = int(input())

valor = 0

for _ in range(0, N):
    valor = 1 / (6 + valor)

valor += 3

print(f"{valor:.10f}")
