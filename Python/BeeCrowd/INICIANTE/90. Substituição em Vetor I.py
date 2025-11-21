X = []
for i in range(0, 10):
    numero = int(input())
    if numero <= 0:
        X.append(1)
        print(f"X[{i}] = {1}")
    else:
        X.append(numero)
        print(f"X[{i}] = {numero}")
