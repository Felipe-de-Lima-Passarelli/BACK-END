T = int(input())

for i in range(0, T):
    B = int(input())
    while B < 0 or B > 100:
        B = int(input())

    A1, D1, L1 = map(int, input().split())
    A2, D2, L2 = map(int, input().split())

    valorDabriel = (A1 + D1)/2
    valorGuarte = (A2 + D2)/2

    if L1%2 == 0:
        valorDabriel += B
    if L2%2 == 0:
        valorGuarte += B

    if valorDabriel > valorGuarte:
        print("Dabriel")
    elif valorDabriel < valorGuarte:
        print("Guarte")
    else:
        print("Empate")
