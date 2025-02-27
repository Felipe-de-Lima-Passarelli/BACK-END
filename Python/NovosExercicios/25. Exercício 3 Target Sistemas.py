faturamento = [1000, 900, 850, 2050, 2320,
               500, 750, 1870, 3000, 1420,
               800, 430, 1210, 995, 1445,
               1010, 4010, 3210, 2500, 1030,
               900, 600, 1950, 2025, 2000,
               2210, 2005, 1990, 3050, 4000]

contador = 0
media = int(sum(faturamento)/len(faturamento))
for valores in faturamento:
    if valores > media:
        contador += 1

print(min(faturamento))
print(max(faturamento))
print(contador)
