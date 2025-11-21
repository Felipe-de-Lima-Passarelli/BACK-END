danomagias = {
    "fire": [200, 20, 30, 50],
    "water": [300, 10, 25, 40],
    "earth": [400, 25, 55, 70],
    "air": [100, 18, 38, 60]
}

T = int(input())

for _ in range(0, T):
    w, h, x0, y0 = map(int, input().split())
    magia, N, cx, cy = input().split()
    magia = str(magia)
    N = int(N)
    cx = int(cx)
    cy = int(cy)

    raiomagia = danomagias[magia][N]
    tamanhoretangulox = x0 + w
    tamanhoretanguloy = y0 + h

    if cx >= tamanhoretangulox:
        pontox = tamanhoretangulox
    elif cx < x0:
        pontox = x0
    else:
        pontox = cx

    if cy >= tamanhoretanguloy:
        pontoy = tamanhoretanguloy
    elif cy < y0:
        pontoy = y0
    else:
        pontoy = cy

    menordistancia = (((pontox - cx)**2) + ((pontoy - cy)**2))**(1/2)
    if raiomagia >= menordistancia:
        print(danomagias[magia][0])
    else:
        print(0)
