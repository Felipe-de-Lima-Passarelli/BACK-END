A, B = map(float, input().split())
while A <= 0 or A > 1000.00 or B <= 0 or B > 1000.00:
    A, B = map(float, input().split())

print(f"{((B*100)/A) - 100.00:.2f}%")
