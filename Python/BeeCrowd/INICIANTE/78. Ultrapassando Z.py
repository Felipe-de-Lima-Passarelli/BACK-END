X = int(input())
Z = int(input())
soma = 0
contador = 0

while not Z > X:
    Z = int(input())

while soma <= Z:
    soma += X
    contador += 1
    X += 1

print(contador)
