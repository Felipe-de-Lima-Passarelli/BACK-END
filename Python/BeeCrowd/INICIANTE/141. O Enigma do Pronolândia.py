N = int(input())
while N <= 0 or N > 9999999999:
    N = int(input())

N = str(N)
print(f"{N[::-1]}")
