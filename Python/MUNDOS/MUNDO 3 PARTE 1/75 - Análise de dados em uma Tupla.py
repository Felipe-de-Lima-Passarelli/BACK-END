num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o primeiro número"))
num3 = int(input("Digite o primeiro número"))
num4 = int(input("Digite o primeiro número"))
lista = (num1, num2, num3, num4)
pares = []

contagem9 = 0

for c in range(0,4):
    if lista[c] == 9:
        contagem9 += 1
    if lista[c] %2 == 0:
        pares.append(lista[c])

if contagem9 > 0:
    print(f"O número 9 apareceu {contagem9} vezes")
else:
    print("O número 9 não apareceu na lista")
if 3 in lista:
        print(f"O primeiro número 3 apareceu na posição {lista.index(3) + 1}")
else:
        print("O número 3 não apareceu na lista")
if len(pares) != 0:
    print(f"Os números pares foram os: {tuple(pares)}")
else:
    print("Não existem números pares na lista")
