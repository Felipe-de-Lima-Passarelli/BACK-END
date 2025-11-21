A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

while A < -100 or B < -100 or C < -100:
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)

if A > B:
    if B <= C:
        print(":)")
    elif B > C:
        if (A - B) > (B - C):
            print(":)")
        else:
            print(":(")
elif B > A:
    if B >= C:
        print(":(")
    elif B < C:
        if (B - A) > (C - B):
            print(":(")
        else:
            print(":)")
elif A == B:
    if C > B:
        print(":)")
    else:
        print(":(")
