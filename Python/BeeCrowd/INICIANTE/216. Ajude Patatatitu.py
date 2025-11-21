N = int(input())
maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for c in range(0, N):
    T = int(input())
    compostos = []
    for _ in range(0, T):
        compostos.append(str(input()))
    U = int(input())
    for _ in range(0, U):
        perigoso = False
        experimento = str(input())
        for nomes in compostos:
            if perigoso:
                break
            palavra = ""
            inicio = []
            for i in range(0, len(experimento)):
                try:
                    if experimento[i] == nomes[0] and experimento[i + 1] == nomes[1]:
                        inicio.append(i)
                except IndexError:
                    pass
            for numeros in inicio:
                try:
                    tamanho = len(nomes)
                    palavra = experimento[numeros:(numeros + tamanho)]
                    if palavra == nomes:
                        try:
                            proximaletra = experimento[numeros + len(nomes)]
                            if maiusculo.find(proximaletra) != -1:
                                perigoso = True
                                break
                            else:
                                pass
                        except IndexError:
                            perigoso = True
                            break

                except IndexError:
                    pass

        if perigoso:
            print("Abortar")
        else:
            print("Prossiga")

    if c != (N -1):
        print()
    else:
        pass
