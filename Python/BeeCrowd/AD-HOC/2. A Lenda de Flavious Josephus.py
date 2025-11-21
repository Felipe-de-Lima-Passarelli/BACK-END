NC = int(input())
contador = 1

for _ in range(0, NC):
    n, k = map(int, input().split())
    k -= 1
    lista_vivos = []
    while n >= 1:
        lista_vivos.append(n)
        n -= 1

    lista_vivos.sort()
    posicao_remover = k

    while len(lista_vivos) != 1:
        while posicao_remover >= len(lista_vivos):
            posicao_remover -= len(lista_vivos)
        lista_vivos.pop(posicao_remover)
        posicao_remover += k

    print(f"Case {contador}: {lista_vivos[0]}")
    contador += 1
