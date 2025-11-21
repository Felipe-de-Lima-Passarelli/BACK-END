while True:
    try:
        N = int(input())
        M, L = map(int, input().split())

        baralhom = []
        baralhol = []

        for _ in range(0, M):
            dados = list(map(int, input().split()))
            while len(dados) != N:
                dados = list(map(int, input().split()))

            baralhom.append(dados)

        for _ in range(0, L):
            dados = list(map(int, input().split()))
            while len(dados) != N:
                dados = list(map(int, input().split()))

            baralhol.append(dados)

        Cm, Cl = map(int, input().split())
        escolham = baralhom[Cm - 1]
        escolhal = baralhol[Cl - 1]

        A = int(input())
        if escolham[A - 1] > escolhal[A - 1]:
            print("Marcos")
        elif escolham[A - 1] < escolhal[A - 1]:
            print("Leonardo")
        else:
            print("Empate")
    except EOFError:
        break
