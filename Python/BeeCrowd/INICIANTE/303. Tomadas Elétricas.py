N = int(input())

for _ in range(0, N):
    K = list(map(int, input().split()))
    print((sum(K) - K[0]) - (K[0] - 1))
