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
cima = 1
baixo = 11

if O == "S":
    for coluna in range(0, 5):
        for linha in range(cima, baixo):
            soma += matriz[linha][coluna]
        cima += 1
        baixo -= 1
    resultado = soma
else:
    contador = 0
    for coluna in range(0, 5):
        for linha in range(cima, baixo):
            soma += matriz[linha][coluna]
            contador += 1
        cima += 1
        baixo -= 1
    resultado = soma/contador

print(f"{resultado:.1f}")
