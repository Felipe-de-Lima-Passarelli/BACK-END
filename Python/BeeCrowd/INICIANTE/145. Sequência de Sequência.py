contagem = 1

while True:
    try:
        N = int(input())
        while N < 0 or N > 200:
            N = int(input())
    except EOFError:
        break

    lista = []
    numero = 1

    for i in range(1, N + 1):
        numero += i

    if N == 0:
        print(f"Caso {contagem}: {numero} numero")
    else:
        print(f"Caso {contagem}: {numero} numeros")

    contagem += 1

    if N == 0:
        lista.append(0)
    elif N == 1:
        lista.append(0)
        lista.append(1)
    else:
        lista.append(0)
        for num in range(0, (N + 1)): # 0 até 2
            for resultado in range(0, num): # 0 até 1
                lista.append(num)

    for posicao, valores in  enumerate(lista):
        if (posicao + 1) == numero:
            print(valores)
        else:
            print(valores, end = " ")
    print()
