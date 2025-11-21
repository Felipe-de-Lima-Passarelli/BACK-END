while True:
    x, y = map(int, input().split())
    x = str(x)
    y = str(y)
    if len(x) >= len(y):
        x = int(x)
        y = f"{int(y):0{len(str(x))}d}"
    else:
        y = int(y)
        x = f"{int(x):0{len(str(y))}d}"
    if not(int(x) or int(y)):
        break

    x = str(x)
    y = str(y)

    contador = 0
    soma = 0
    for i in range((len(x) - 1), -1, -1):
        if (int(x[i]) + int(y[i])) + soma >= 10:
            contador += 1
            soma = 1
        else:
            soma = 0

    if contador == 0:
        print("No carry operation.")
    elif contador == 1:
        print(f"{contador} carry operation.")
    else:
        print(f"{contador} carry operations.")
