N = int(input())
verba_governo = 0
verba_universidade = 0

for _ in range(0, N):
    T, C = input().split()
    T = str(T)
    C = int(C)

    if T == "V":
        verba_governo += C
    else:
        verba_universidade += C

if verba_universidade > verba_governo:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")
