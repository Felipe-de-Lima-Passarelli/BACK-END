N = int(input())

if N == 1 or N == 2:
    print(N)
elif N == 3:
    print(N + 1)
else:
    diferenca = N - 3
    dados = [1, 2, 4]

    combinacao_2 = (N * (N - 1)) // 2
    combinacao_4 = (N * (N - 1) * (N - 2) * (N - 3)) // 24 if N >= 4 else 0
    print(1 + combinacao_2 + combinacao_4)
