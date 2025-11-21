A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

lista = [A, B, C]
novalista = sorted(lista, reverse = True)

if novalista[1] + novalista[2] > novalista[0]:
    print(f"Perimetro = {sum(lista)}")
else:
    print(f"Area = {((A+B)*C)/2}")
