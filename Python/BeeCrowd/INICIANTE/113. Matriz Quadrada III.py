while True:
    N = int(input())
    while N < 0 or N > 15:
        N = int(input())

    if N == 0:
        break

    matriz = []

    for i in range(N):
        linha = []
        for j in range(N):
            valor = 2 ** (i + j)
            linha.append(valor)
        matriz.append(linha)

    maior = 0
    for linha in matriz:
        for num in linha:
            if num > maior:
                maior = num

    largura = (len(str(maior)))

    for linha in matriz:
        for num in linha:
            if num == max(linha):
                print(f"{num:>{largura}}")
            else:
                print(f"{num:>{largura}}", end = " ")
    print()