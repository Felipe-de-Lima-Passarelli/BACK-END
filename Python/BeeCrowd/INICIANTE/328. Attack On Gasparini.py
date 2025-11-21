n, x = map(int, input().split())
tamanhos_letras = str(input())
tamanhos_numeros = []
p, m, g = map(int, input().split())
muralhas = [x]

for letras in tamanhos_letras:
    if letras == "P":
        tamanhos_numeros.append(p)
    elif letras == "M":
        tamanhos_numeros.append(m)
    else:
        tamanhos_numeros.append(g)

for i in range(0, n):
    c = 0
    while tamanhos_numeros[i] > muralhas[c]:
        muralhas.append(x)
        c += 1
    muralhas[c] -= tamanhos_numeros[i]

muralhas.append(x)
print(muralhas.index(x))
