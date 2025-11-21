T = int(input())

for i in range(0, T):
    PA, PB, G1, G2 = input().split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)

    anos = 0

    while PA <= PB:
        PA += int(PA * G1 // 100)
        PB += int(PB * G2 // 100)
        anos += 1

        if anos > 100:
            break

    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")
