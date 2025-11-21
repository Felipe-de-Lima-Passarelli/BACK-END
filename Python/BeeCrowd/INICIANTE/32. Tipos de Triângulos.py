A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
while A < 0 or B < 0 or C < 0:
    A, B, C = input().split()
    A = float(A)
    B = float(B)
    C = float(C)

lista = [A, B, C]
novalista = sorted(lista, reverse = True)

A = novalista[0]
B = novalista[1]
C = novalista[2]

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == (B**2 + C**2):
        print("TRIANGULO RETANGULO")

    if A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")

    if A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")

    if A == B != C or B == C != A or A == C != B:
        print("TRIANGULO ISOSCELES")
