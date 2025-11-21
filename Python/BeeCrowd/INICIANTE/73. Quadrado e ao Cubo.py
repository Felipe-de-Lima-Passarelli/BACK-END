N = int(input())
c = 1

while N <= 1 or N >= 1000:
    N = int(input())

for i in range(0, N):
    print(f"{c} {c**2} {c**3}")
    c += 1
