maior = 0
posicaomaior = 0
posicaofinalmaior = 0

for i in range(0, 100):
    x = int(input())
    posicaomaior += 1
    if x > maior:
        maior = x
        posicaofinalmaior = posicaomaior

print(maior)
print(posicaofinalmaior)
