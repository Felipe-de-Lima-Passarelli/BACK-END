C = int(input())
while C < 0 or C > 11:
    C = int(input())

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

if T == "S":
    resultado = 0
    for i in range(0, 12):
        resultado += matriz[i][C]
else:
    soma = 0
    for i in range(0, 12):
        soma += matriz[i][C]
    resultado = soma/12

print(f"{resultado:.1f}")
