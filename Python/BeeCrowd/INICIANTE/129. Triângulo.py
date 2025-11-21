A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

while A < 1 or A > 100 or B < 1 or B > 100 or C < 1 or C > 100 or D < 1 or D > 100:
    A, B, C, D = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)

contador = 0
while True:
    if A + B > C:
        contador += 1

    if A + C > B:
        contador += 1

    if B + C > A:
        contador += 1

    if contador == 3:
        print("S")
        break

    contador = 0

    if A + B > D:
        contador += 1

    if A + D > B:
        contador += 1

    if B + D > A:
        contador += 1

    if contador == 3:
        print("S")
        break

    contador = 0

    if A + C > D:
        contador += 1

    if A + D > C:
        contador += 1

    if C + D > A:
        contador += 1

    if contador == 3:
        print("S")
        break

    contador = 0

    if B + C > D:
        contador += 1

    if B + D > C:
        contador += 1

    if C + D > B:
        contador += 1

    if contador == 3:
        print("S")
        break
    else:
        print("N")
        break
