while True:
    K = int(input())
    if K == 0:
        break

    N, M = map(int, input().split())
    for _ in range(0, K):
        X, Y = map(int, input().split())
        if X == N or Y == M:
            print("divisa")
        else:
            if X > N and Y > M:
                print("NE")
            elif X > N and Y < M:
                print("SE")
            elif X < N and Y > M:
                print("NO")
            else:
                print("SO")
