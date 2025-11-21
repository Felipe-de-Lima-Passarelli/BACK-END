N = int(input())
while N < 1 or N > 100:
    N = int(input())

matriz = []
for c in range(0, (N + 1)):
    linha = [0] * (N + 1)
    matriz.append(linha)

for i in range(0, (N + 1)):
    dados = list(map(int, input().split()))
    c = 0
    for numeros in dados:
        matriz[i][c] = numeros
        c += 1

linhas = 0
resposta = []

for i in range(0, N):
    colunas = 0
    for _ in range(0, N):
        contagem = 0
        a = matriz[linhas + i][colunas]
        b = matriz[linhas + i][colunas + 1]
        c = matriz[linhas + i + 1][colunas]
        d = matriz[linhas + i + 1][colunas + 1]
        if a == 1:
            contagem += 1
        if b == 1:
            contagem += 1
        if c == 1:
            contagem += 1
        if d == 1:
            contagem += 1
        colunas += 1

        if contagem >= 2:
            resposta.append("S")
        else:
            resposta.append("U")

contagemfinal = 0
for letra in resposta:
    contagemfinal += 1
    if contagemfinal == N:
        print(letra)
        contagemfinal = 0
    else:
        print(letra, end = "")
