O = str(input())
while O != "S" and O != "M":
    O = str(input())

matriz = []
for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)

soma = 0

if O == "S":
    for linha in range(1, 12):
        c = 0
        while c < linha:
            soma += matriz[linha][c]
            c += 1
    resultado = soma
else:
    contador = 0
    for linha in range(1, 12):
        c = 0
        while c < linha:
            soma += matriz[linha][c]
            c += 1
            contador += 1
    resultado = soma/contador

print(f"{resultado:.1f}")
