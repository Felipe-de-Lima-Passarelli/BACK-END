N = int(input())

for _ in range(0, N):
    M = int(input())
    lista = []
    dados = list(map(int, input().split()))
    respostafinal = []
    for numeros in dados:
        if numeros%2 != 0:
            lista.append(numeros)
    lista.sort(reverse = True)

    while True:
        if len(lista) == 0:
            break
        elif len(lista) >= 2:
            respostafinal.append(max(lista))
            respostafinal.append(min(lista))
            lista.pop(0)
            lista.pop(-1)
        else:
            respostafinal.append(lista[0])
            break

    print(*respostafinal)
