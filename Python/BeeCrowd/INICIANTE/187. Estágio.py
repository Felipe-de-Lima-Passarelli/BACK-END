while True:
    try:
        M = int(input())
        notas = []
        cargashorarias = []
        for _ in range(0, M):
            N, C = map(int, input().split())
            notas.append(N)
            cargashorarias.append(C)

        cima = 0
        baixo = 0
        for i in range(0, M):
            cima += notas[i] * cargashorarias[i]
            baixo += cargashorarias[i]
        baixo *= 100

        print(f"{cima/baixo:.4f}")

    except EOFError:
        break
