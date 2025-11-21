N = int(input())
pesquisas = []
for _ in range(0, N):
    pesquisas.append(str(input()).lower())

Q = int(input())
for _ in range(0, Q):
    contador = 0
    tamanho = 0
    frase = str(input())
    for palavras in pesquisas:
        if frase == palavras[0:len(frase)]:
            contador += 1
            if len(palavras) > tamanho:
                tamanho = len(palavras)

    if contador == 0:
        print(-1)
    else:
        print(f"{contador} {tamanho}")
