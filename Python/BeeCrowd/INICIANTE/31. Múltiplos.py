A, B = input().split()
A = int(A)
B = int(B)

lista = [A, B]
novalista = sorted(lista, reverse = True)
if novalista[0]%novalista[1] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
