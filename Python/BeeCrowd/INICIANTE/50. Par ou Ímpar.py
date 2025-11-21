N = int(input())

for i in range(0, N):
    x = int(input())
    saida = []
    if x == 0:
        print("NULL")
    elif x%2 == 0:
        saida.append("EVEN")
        if x > 0:
            print(f"{saida[0]} POSITIVE")
        else:
            print(f"{saida[0]} NEGATIVE")
    else:
        saida.append("ODD")
        if x > 0:
            print(f"{saida[0]} POSITIVE")
        else:
            print(f"{saida[0]} NEGATIVE")
