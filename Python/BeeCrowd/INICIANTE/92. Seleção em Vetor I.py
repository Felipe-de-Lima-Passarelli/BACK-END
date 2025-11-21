A = []

for i in range(0, 100):
    X = float(input())
    A.append(X)
    if X <= 10:
        print(f"A[{i}] = {X:.1f}")
