contagempositivo = 0
for i in range(0, 6):
    x = float(input())
    if x > 0:
        contagempositivo += 1
    while x == 0:
        x = float(input())
        if x > 0:
            contagempositivo += 1

print(f"{contagempositivo} valores positivos")
