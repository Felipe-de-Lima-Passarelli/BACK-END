import math

while True:
    try:
        Xf, Yf, Xi, Yi, Vi, R1, R2 = map(int, input().split())
    except EOFError:
        break

    distancia = math.sqrt((Xf - Xi) ** 2 + (Yf - Yi) ** 2)

    distancia_invasor = Vi * 1.5
    alcance_ultimate = R1 + R2

    if distancia + distancia_invasor <= alcance_ultimate:
        print("Y")
    else:
        print("N")
