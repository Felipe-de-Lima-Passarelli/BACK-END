L = int(input())
while L < 0 or L > 11:
    L = int(input())

T = str(input())
while T != "S" and T != "M":
    T = str(input())

matriz = []

for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)

linhaescolhida = matriz[L]

if T == "S":
    resultado = sum(linhaescolhida)
else:
    resultado = sum(linhaescolhida)/len(linhaescolhida)

print(f"{resultado:.1f}")
