while True:
    try:
        T = int(input())
        while T < 2 or T > 50:
            T = int(input())
    except EOFError:
        break

    contas = []
    errados = []
    for _ in range(0, T):
        X, Y, Z = map(str ,input().replace("=", " ").split())
        frase = f"{X}{'OPERADOR'}{Y} == {Z}"
        contas.append(frase)

    for _ in range(0, T):
        dados = input().split()
        nome = dados[0:-2]
        N = ""
        for palavras in nome:
            N += palavras + " "
        N = str(N[0:-1])
        E = int(dados[-2])
        R = str(dados[-1])

        x = contas[E - 1]
        impossivel = True
        if R == "I":
            y = x[:]
            y = y.replace("OPERADOR", "+")
            if eval(y):
                impossivel = False
            y = x[:]
            y = y.replace("OPERADOR", "-")
            if eval(y):
                impossivel = False
            y = y.replace("OPERADOR", "*")
            if eval(y):
                impossivel = False

            if not impossivel:
                errados.append(N)
        else:
            x = x.replace("OPERADOR", R)
            if not eval(x):
                errados.append(N)

    errados.sort()

    if len(errados) == T:
        print("None Shall Pass!")
    elif len(errados) == 0:
        print("You Shall All Pass!")
    else:
        for nomes in errados:
            if nomes != errados[len(errados) - 1]:
                print(nomes, end = " ")
            else:
                print(nomes)
