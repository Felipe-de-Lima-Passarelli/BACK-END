from time import sleep

matriz = [[], [], []]

print(25*"-=")
print("Vamos montar uma matriz?")
print(10*"-=")
sleep(2)

for c in range(0,3):
    matriz[0].append(int(input(f"Digite um valor para a posição [0,{c}]: ")))

for c in range(0,3):
    matriz[1].append(int(input(f"Digite um valor para a posição [1,{c}]: ")))

for c in range(0,3):
    matriz[2].append(int(input(f"Digite um valor para a posição [2,{c}]: ")))

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

determinante = (((matriz[0][0] * matriz[1][1] * matriz[2][2]) +
                 (matriz[0][1] * matriz[1][2] * matriz[2][0]) +
                 (matriz[0][2] * matriz[1][0] * matriz[2][1])) -
                ((matriz[0][2] * matriz[1][1] * matriz[2][0]) +
                 (matriz[0][0] * matriz[1][2] * matriz[2][1]) +
                 (matriz[0][1] * matriz[1][0] * matriz[2][2])))

print("CALCULANDO DETERMINANTE")
sleep(2)
print(f"A determinante da sua matriz teve um valor total de {determinante}")
