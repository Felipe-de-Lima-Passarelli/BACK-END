T1, T2, T3, T4 = map(int, input().split())
while T1 < 2 or T1 > 6 or T2 < 2 or T2 > 6 or T3 < 2 or T3 > 6 or T4 < 2 or T4 > 6:
    T1, T2, T3, T4 = map(int, input().split())

print((T1+T2+T3+T4) - 3)
