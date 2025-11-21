N = int(input())
X = []
menor = 999999
valores = input().split()
while len(valores) < N:
    valores = input().split()

for i in valores:
    X.append(int(i))
    if int(i) < menor:
        menor = int(i)
    if len(X) == N:
        break

print(f"Menor valor: {menor}")
print(f"Posicao: {X.index(menor)}")
