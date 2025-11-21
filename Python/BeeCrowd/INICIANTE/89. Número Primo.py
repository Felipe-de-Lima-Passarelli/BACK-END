N = int(input())
while N < 1 or N > 100:
    N = int(input())

for i in range(N):
    X = int(input())
    while X <= 1 or X > 10000000:
        X = int(input())

    primo = 0
    for num in range(1, X+1):
        if X%num == 0:
            primo += 1

    if primo == 2:
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")
