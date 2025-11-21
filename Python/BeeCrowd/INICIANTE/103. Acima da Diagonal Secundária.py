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
    for linha in range(0, 11):
        for coluna in range(0, (11 - linha)):
            soma += matriz[linha][coluna]
    resultado = soma
else:
    contador = 0
    for linha in range(0, 11):
        for coluna in range(0, (11 - linha)):
            soma += matriz[linha][coluna]
            contador += 1
    resultado = soma/contador

print(f"{resultado:.1f}")
