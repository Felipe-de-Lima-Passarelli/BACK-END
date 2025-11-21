N, L = map(int ,input().split())
while N < 3 or N > 1000000 or L < 1 or L > 4000:
    N, L = map(int, input().split())

print(N*L)
