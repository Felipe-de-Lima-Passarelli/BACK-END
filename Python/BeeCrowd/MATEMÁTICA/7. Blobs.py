N = int(input())

for _ in range(0, N):
    dias = 0
    C = float(input())
    while C > 1:
        C /= 2
        dias += 1
    print(f"{dias} dias")
