L = int(input())
C = int(input())

branca = True

for linha in range(1, (L + 1)):
    if linha%2 != 0:
        branca = True
    else:
        branca = False

for coluna in range(1, (C + 1)):
    if L%2 == 0:
        if coluna%2 != 0:
            branca = False
        else:
            branca = True
    else:
        if coluna%2 != 0:
            branca = True
        else:
            branca = False

if branca:
    print(1)
else:
    print(0)
