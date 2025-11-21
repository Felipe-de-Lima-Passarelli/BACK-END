N = int(input())
naves = []

for _ in range(0, N):
    x, y, z = map(int, input().split())
    naves.append((x, y, z))

for i in range(0, len(naves)):
    menor = 999
    for nave in naves:
        if nave != naves[i]:
            distancia = ((nave[0] - naves[i][0])**2 + (nave[1] - naves[i][1])**2 + (nave[2] - naves[i][2])**2)**(1/2)
            if distancia < menor:
                menor = distancia
    if menor <= 20:
        print("A")
    elif menor <= 50:
        print("B")
    else:
        print("M")
