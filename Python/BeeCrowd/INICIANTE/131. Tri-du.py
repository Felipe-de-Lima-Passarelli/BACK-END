A, B = map(int, input().split())
while A < 1 or A > 30 or B < 1 or B > 13:
    A, B = map(int, input().split())

if A == B:
    print(A)

if A > B:
    print(A)
elif A < B:
    print(B)
