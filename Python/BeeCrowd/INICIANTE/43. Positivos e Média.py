contagempositivo = 0
listamedia = []
for i in range(0, 6):
    x = float(input())
    if x > 0:
        contagempositivo += 1
        listamedia.append(x)
    while x == 0:
        x = float(input())
        if x > 0:
            contagempositivo += 1
media = sum(listamedia)/len(listamedia)

print(f"{contagempositivo} valores positivos")
print(f"{media:.1f}")
