N = []
X = float(input())
for i in range(0, 100):
    N.append(X)
    print(f"N[{i}] = {X:.4f}")
    X /= 2
