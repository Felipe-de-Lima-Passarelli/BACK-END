from random import randint
maior = 0
menor = 0

x = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Os números sorteados foram {x}")

for c in range(0, 5):
    if c == 0:
        maior = x[c]
        menor = x[c]
    else:
        if x[c] > maior:
            maior = x[c]
        if x[c] < menor:
            menor = x[c]

print(f"O menor valor sorteado foi {menor}")
print(f"O maior valor sorteado foi {maior}")
