porcoes = []
valores = [300, 1500, 600, 1000, 150]
total = 0

for _ in range(0, 5):
    quantidade = int(input())
    porcoes.append(quantidade)

for i in range(0, len(porcoes)):
    total += porcoes[i] * valores[i]

print(total + 225)
