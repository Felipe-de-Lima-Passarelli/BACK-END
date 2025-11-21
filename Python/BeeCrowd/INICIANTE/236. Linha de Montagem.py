while True:
    try:
        N = int(input())
        e1, e2 = map(int, input().split())
        linha1 = list(map(int, input().split()))
        linha2 = list(map(int, input().split()))
        transicao1_2 = list(map(int, input().split()))
        transicao2_1 = list(map(int, input().split()))
        x1, x2 = map(int, input().split())

        dp1 = [0] * N
        dp2 = [0] * N

        dp1[0] = e1 + linha1[0]
        dp2[0] = e2 + linha2[0]

        for i in range(1, N):
            dp1[i] = min(dp1[i-1] + linha1[i], dp2[i-1] + transicao2_1[i-1] + linha1[i])
            dp2[i] = min(dp2[i-1] + linha2[i], dp1[i-1] + transicao1_2[i-1] + linha2[i])

        resultado = min(dp1[N-1] + x1, dp2[N-1] + x2)
        print(resultado)

    except EOFError:
        break
