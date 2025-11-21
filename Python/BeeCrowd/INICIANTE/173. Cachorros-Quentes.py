H, P = map(int, input().split())
while H < 1 or H > 1000 or P < 1 or P > 1000:
    H, P = map(int, input().split())

print(f"{(H/P):.2f}")
