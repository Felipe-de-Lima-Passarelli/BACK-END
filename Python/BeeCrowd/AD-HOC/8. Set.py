while True:
    N = int(input())
    if N == 0:
        break
    cartas = []
    resposta_final = 0

    for _ in range(N):
        quantidade, formato = input().split()
        if formato.endswith("s"):
            formato = formato[:-1]
        cartas.append([quantidade, formato])

    while len(cartas) >= 3:
        encontrou_set = False

        for i in range(len(cartas) - 2):
            for j in range(i + 1, len(cartas) - 1):
                for k in range(j + 1, len(cartas)):
                    c1, c2, c3 = cartas[i], cartas[j], cartas[k]

                    numeros = {c1[0], c2[0], c3[0]}
                    formas = {c1[1], c2[1], c3[1]}

                    if (len(numeros) == 1 or len(numeros) == 3) and (len(formas) == 1 or len(formas) == 3):
                        cartas = [c for idx, c in enumerate(cartas) if idx not in (i, j, k)]
                        resposta_final += 1
                        encontrou_set = True
                        break
                if encontrou_set:
                    break
            if encontrou_set:
                break

        if not encontrou_set:
            break

    print(resposta_final)
