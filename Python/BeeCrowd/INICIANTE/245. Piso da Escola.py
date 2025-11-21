L = int(input())
C = int(input())

tipo1 = 0
tipo2 = ((C - 1) * 2) + ((L - 1) * 2)

if C != 1 or L != 1:
    for i in range(0, L):
        if i != (L - 1):
            tipo1 += C + (C - 1)
        else:
            tipo1 += C
else:
    tipo1 = 1

print(tipo1)
print(tipo2)
