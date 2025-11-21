while True:
    try:
        N, M = map(int, input().split())
    except EOFError:
        break

    matriz = []
    linha1 = 0
    coluna1 = 0
    linha2 = 0
    coluna2 = 0
    for i in range(0, N):
        linha = []
        dados = list(map(int,input().split()))
        if 1 in dados:
            linha1 = i
            coluna1 = dados.index(1)
        if 2 in dados:
            linha2 = i
            coluna2 = dados.index(2)

        while len(dados) != M:
            dados = list(map(int, input().split()))
        for numeros in dados:
            linha.append(numeros)
        matriz.append(linha)

    contagem = 0

    if linha1 > linha2:
        contagem+= linha1 - linha2
    if coluna1 > coluna2:
        contagem += coluna1 - coluna2
    if linha1 < linha2:
        contagem += linha2 - linha1
    if coluna1 < coluna2:
        contagem+= coluna2 - coluna1

    print(contagem)
