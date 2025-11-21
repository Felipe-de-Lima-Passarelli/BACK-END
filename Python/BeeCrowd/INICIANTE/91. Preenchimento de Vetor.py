X = []
V = int(input())
while V > 50:
    V = int(input())

for i in range(0, 10):
    X.append(V)
    V *= 2
    print(f"N[{i}] = {X[i]}")
