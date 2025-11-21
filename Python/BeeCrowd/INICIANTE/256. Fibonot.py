K = int(input())

fibonacci = [1, 1]
x1 = 1
x2 = 1
numero = 3

for _ in range(0, K):
    fibonacci.append(x1 + x2)
    x1, x2 = x2, (x1 + x2)

numerosresposta = []

while len(numerosresposta) != K:
    numero += 1
    if numero not in fibonacci:
        numerosresposta.append(numero)

print(numerosresposta[-1])
