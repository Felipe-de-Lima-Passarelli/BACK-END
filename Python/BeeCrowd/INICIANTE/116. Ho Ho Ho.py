N = int(input())
while N <= 0 or N > 1000000:
    N = int(input())

for i in range(0, N):
    if i == (N - 1):
        print(f"Ho!")
    else:
        print(f"Ho ", end = "")
