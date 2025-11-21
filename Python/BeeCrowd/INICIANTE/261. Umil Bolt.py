while True:
    try:
        T = int(input())
        menor = 0
        for i in range(0, T):
            tempo = float(input())
            if i == 0:
                menor = tempo
            else:
                if tempo < menor:
                    menor = tempo
        print(menor)
    except EOFError:
        break
