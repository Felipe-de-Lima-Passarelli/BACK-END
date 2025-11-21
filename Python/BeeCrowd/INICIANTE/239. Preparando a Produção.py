while True:
    try:
        N = int(input())
        pacote = list(map(int, input().split()))
        pacotes = pacote[:]
        tempo = list(map(int, input().split()))
        tempogasto = 0

        for i in range(1, (N + 1)):
            while pacotes[i - 1] != i:
                posicaoatual = pacotes.index(i)
                posicaoanterior = posicaoatual - 1
                pacotes[posicaoatual] = pacotes[posicaoanterior]
                pacotes[posicaoanterior] = i
                tempogasto += tempo[pacote.index(i)] + tempo[pacote.index(pacotes[posicaoatual])]
        print(tempogasto)

    except EOFError:
        break
