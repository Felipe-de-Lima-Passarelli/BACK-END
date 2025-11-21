while True:
    A, B = map(int, input().split())
    if not(A or B):
        break

    numeros_utilizados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(A, (B + 1)):
        for letras in str(i):
            numeros_utilizados[int(letras)] += 1

    print(*numeros_utilizados)
