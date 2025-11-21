C = int(input())

for i in range(0, C):
    N = int(input())
    while N < 1 or N > 1000:
        N = int(input())

    if N%2 == 0:
        print(0)
    else:
        print(1)
