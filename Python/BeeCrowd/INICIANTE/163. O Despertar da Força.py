N, M = map(int, input().split())
while N < 3 or N > 1000 or M < 3 or M > 1000:
    N, M = map(int, input().split())

resposta = 0, 0
matriz = []

for i in range(0, N):
    linha = [0] * M
    matriz.append(linha)

for linha in range(0, N):
    dados = list(map(int, input().split()))
    c = 0
    for num in dados:
        matriz[linha][c] = num
        c += 1

for finallinha in range(1, (N - 1)):
    for colunafinal in range(1, (M - 1)):
        if matriz[finallinha][colunafinal] == 42:
                if (matriz[finallinha - 1][colunafinal] == 7
                and matriz[finallinha - 1][colunafinal + 1] == 7
                and matriz[finallinha - 1][colunafinal - 1] == 7
                and matriz[finallinha][colunafinal - 1] == 7
                and matriz[finallinha][colunafinal + 1] == 7
                and matriz[finallinha + 1][colunafinal] == 7
                and matriz[finallinha + 1][colunafinal - 1] == 7
                and matriz[finallinha + 1][colunafinal + 1] == 7):
                    resposta = (finallinha + 1), (colunafinal + 1)

print(resposta[0], resposta[1])
