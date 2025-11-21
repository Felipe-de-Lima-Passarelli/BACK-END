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
esquerda = 5
direita = 7

if O == "S":
    for linha in range(7, 12):
        for coluna in range(esquerda, direita):
            soma += matriz[linha][coluna]
        esquerda -= 1
        direita += 1
    resultado = soma
else:
    contador = 0
    for linha in range(7, 12):
        for coluna in range(esquerda, direita):
            soma += matriz[linha][coluna]
            contador += 1
        esquerda -= 1
        direita += 1
    resultado = soma/contador

print(f"{resultado:.1f}")
