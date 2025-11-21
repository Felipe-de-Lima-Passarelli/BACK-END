F1, F2 = map(float, input().split())
T = (1 + F1 / 100) * (1 + F2 / 100) - 1

print(f"{T * 100:.6f}")
