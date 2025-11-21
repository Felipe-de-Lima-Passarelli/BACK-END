while True:
    try:
        M = int(input())
        moedas = []
        for _ in range(0, M):
            moeda = int(input())
            moedas.insert(0, moeda)

        salto = int(input())
        soma = 0
        c = 0

        for _ in range(0, len(moedas)):
            if (c+1) > len(moedas):
                break
            soma += moedas[c]
            c += salto

        if soma == 1:
            print("Bad boy! I’ll hit you.")
        else:
            contagem = 0
            for i in range(1, (soma + 1)):
                if soma%i == 0:
                    contagem += 1

            if contagem == 2:
                print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
            else:
                print("Bad boy! I’ll hit you.")

    except EOFError:
        break
