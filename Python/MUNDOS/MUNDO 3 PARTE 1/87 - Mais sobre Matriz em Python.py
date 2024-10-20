from time import sleep

matriz = [[], [], []]
pares = 0
maior = 0

print(25*"-=")
print("Vamos montar uma matriz?")
print(10*"-=")
sleep(2)

for c in range(0,3):
    matriz[0].append(int(input(f"Digite um valor para a posição [0,{c}]: ")))
    if matriz[0][c] %2 == 0:
        pares += matriz[0][c]

for c in range(0,3):
    matriz[1].append(int(input(f"Digite um valor para a posição [1,{c}]: ")))
    if matriz[1][c] %2 == 0:
        pares += matriz[1][c]
    if matriz[1][c] > maior:
        maior = matriz[1][c]

for c in range(0,3):
    matriz[2].append(int(input(f"Digite um valor para a posição [2,{c}]: ")))
    if matriz[2][c] %2 == 0:
        pares += matriz[2][c]

print("ANALISANDO A MATRIZ")
sleep(2)

print(25*"-=")
print(f"[  {matriz[0][0]:^3}  ]", end = "")
print(f"[  {matriz[0][1]:^3}  ]", end = "")
print(f"[  {matriz[0][2]:^3}  ]")

print(f"[  {matriz[1][0]:^3}  ]", end = "")
print(f"[  {matriz[1][1]:^3}  ]", end = "")
print(f"[  {matriz[1][2]:^3}  ]")

print(f"[  {matriz[2][0]:^3}  ]", end = "")
print(f"[  {matriz[2][1]:^3}  ]", end = "")
print(f"[  {matriz[2][2]:^3}  ]")
print(25*"-=")

print(f"A soma dos números pares deu: {pares}")
print(f"A soma dos valores da terceira coluna deu: {(matriz[0][2] + matriz[1][2] + matriz[2][2])}")
print(f"O maior valor da segunda linha foi o: {maior}")
