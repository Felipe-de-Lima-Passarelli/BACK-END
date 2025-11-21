while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    Cartas_A = list(map(int, input().split()))
    Cartas_B = list(map(int, input().split()))

    for numeros in Cartas_A:
        if Cartas_A.count(numeros) > 1:
            Cartas_A.remove(numeros)
    for numeros in Cartas_B:
        if Cartas_B.count(numeros) > 1:
            Cartas_B.remove(numeros)

    if len(Cartas_B) <= len(Cartas_A):
        contador = 0
        for numeros in Cartas_B:
            if numeros not in Cartas_A:
                contador += 1
        print(contador)
    else:
        contador = 0
        for numeros in Cartas_A:
            if numeros not in Cartas_B:
                contador += 1
        print(contador)
