N = int(input())
while N <= 1 or N > 100:
    N = int(input())

dados = list(map(int, input().split()))

lista = []

for i in range(0, len(dados)):
    if i != (len(dados) - 1):
        if dados[i] < dados[i + 1]:
            lista.append(True)
        elif dados[i] > dados[i + 1]:
            lista.append(False)
        else:
            lista.append(10)
    else:
        pass

alternando = True

for i in range(0, (len(lista) - 1)):
    if lista[i] == lista[i + 1]:
        alternando = False
        break

if alternando and 10 not in lista:
    print(1)
else:
    print(0)
