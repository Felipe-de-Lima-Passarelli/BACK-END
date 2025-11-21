X = float(input())
contador = 0
sinal = "+"

if X != 0:
    if abs(X) >= 10:
        while abs(X) > 10:
            X /= 10
            contador += 1
    elif abs(X) < 1:
        while abs(X) < 1:
            X *= 10
            contador +=1
        sinal = "-"

    if X > 0:
        print(f"+{X:.4f}E{sinal}{contador:02}")
    else:
        print(f"{X:.4f}E{sinal}{contador:02}")

if X == 0:
    X = str(X)
    if X[0] == "-":
        print(f"-{0:.4f}E{sinal}{0:02}")
    else:
        print(f"+{0:.4f}E{sinal}{0:02}")
