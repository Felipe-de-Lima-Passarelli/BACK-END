contagempares = 0
contagemimpares = 0
contagempositivos = 0
contagemnegativos = 0
for i in range(0, 5):
    x = int(input())

    if x%2 == 0:
        contagempares += 1
    else:
        contagemimpares += 1
    if x > 0 and x != 0:
        contagempositivos += 1
    elif x < 0 and x != 0:
        contagemnegativos += 1

print(f"{contagempares} valor(es) par(es)")
print(f"{contagemimpares} valor(es) impar(es)")
print(f"{contagempositivos} valor(es) positivo(s)")
print(f"{contagemnegativos} valor(es) negativo(s)")
