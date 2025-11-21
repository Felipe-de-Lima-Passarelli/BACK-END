N = int(input())
c = 1

while N <= 1 or N >= 1000:
    N = int(input())

for i in range(0, N):
    print(f"{c} {c**2} {c**3}")
    print(f"{c} {(c**2) + 1} {(c**3) + 1}")
    c += 1
