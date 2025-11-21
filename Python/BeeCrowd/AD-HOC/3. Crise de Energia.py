while True:
    N = int(input())
    if N == 0:
        break

    resposta = 1
    while True:
        lista = [i for i in range(1, N+1)]
        lista_teste = lista[:]
        posicao = 0

        if N == 13:
            print(1)
            break

        while len(lista_teste) != 1:
            lista_teste.pop(posicao)
            posicao += resposta
            while posicao > (len(lista_teste) - 1):
                posicao -= len(lista_teste)

        if lista_teste[0] == 13:
            print(resposta + 1)
            break
        else:
            resposta += 1
