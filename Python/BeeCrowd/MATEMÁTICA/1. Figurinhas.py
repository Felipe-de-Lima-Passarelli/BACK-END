from math import gcd

N = int(input())

for _ in range(0, N):
    F1, F2 = map(int, input().split())
    print(gcd(F1,F2))
