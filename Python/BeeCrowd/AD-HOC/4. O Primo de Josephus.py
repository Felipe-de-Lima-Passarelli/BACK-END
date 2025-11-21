while True:
    n = int(input())
    if n == 0:
        break

    lista_vivos = []
    while n >= 1 :
        lista_vivos.append(n)
        n -= 1
    lista_vivos.sort()

    primos = []
    num = 2

    while len(primos) != len(lista_vivos):
        primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            primos.append(num)
        num += 1
    posicao = 0

    while len(lista_vivos) != 1:
        m = primos.pop(0)
        posicao = (posicao + m - 1) % len(lista_vivos)
        lista_vivos.pop(posicao)

    print(lista_vivos[0])
