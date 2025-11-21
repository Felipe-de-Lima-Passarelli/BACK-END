N = []
T = int(input())
c = 0
while T < 2 or T > 50:
    T = int(input())

while True:
    for num in range(0, T):
        N.append(num)
        print(f"N[{c}] = {num}")
        c += 1
        if len(N) == 1000:
            break
    if len(N) == 1000:
        break
