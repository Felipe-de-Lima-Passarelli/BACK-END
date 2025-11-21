A, B, C = map(int, input().split())
while A < 1 or A > 1000 or B < 1 or B > 1000 or C < 1 or C > 1000:
    A, B, C = map(int, input().split())

if A == B or A == C or B == C:
    print("S")
elif (A + B) == C or (A + C) == B or (B + C) == A:
    print("S")
else:
    print("N")
