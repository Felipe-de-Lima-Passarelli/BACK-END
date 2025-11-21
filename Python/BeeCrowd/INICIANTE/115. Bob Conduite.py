T = int(input())

while T > 10000 or T <= 0:
    T = int(input())

for i in range(0, T):
    R1, R2 = input().split()
    R1 = int(R1)
    R2 = int(R2)

    print(f"{R1 + R2}")
