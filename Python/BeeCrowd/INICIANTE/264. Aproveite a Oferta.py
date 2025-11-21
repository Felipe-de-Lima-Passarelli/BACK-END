T = int(input())

for _ in range(0, T):
    N, K = map(int, input().split())
    if N >= K:
        X = int(N/K) + (N - (int(N/K) * K))
    else:
        X = N

    print(X)
