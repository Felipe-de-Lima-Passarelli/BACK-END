N = int(input())
contador = 0

for _ in range(0, N):
    portacarro = int(input())
    if portacarro != 1:
        contador += 1

print(contador)
