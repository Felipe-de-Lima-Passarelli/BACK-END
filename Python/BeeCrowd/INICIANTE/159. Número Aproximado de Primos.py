from math import log

n = int(input())
while n < 17 or n > 10**9:
    n = int(input())

P = n/log(n)
M = 1.25506 * P

print(f"{P:.1f} {M:.1f}")
