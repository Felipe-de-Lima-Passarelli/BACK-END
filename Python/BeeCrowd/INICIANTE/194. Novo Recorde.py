while True:
    try:
        N = int(input())
        duracao = []
        distancia = []
        velocidademedia = 0

        for _ in range(0, N):
            Ti, Di = map(int, input().split())
            duracao.append(Ti)
            distancia.append(Di)

        for i in range(0, N):
            if i == 0:
                print(1)
                velocidademedia = distancia[0] / duracao[0]
            else:
                contador = 0
                for numeros in distancia:
                    if numeros / duracao[contador] > velocidademedia:
                        print(contador + 1)
                        velocidademedia = numeros / duracao[contador]
                    contador += 1

    except EOFError:
        break
