while True:
    try:
        C, N = map(int, input().split())
        cifra1 = input().strip()
        cifra2 = input().strip()

        mapa_cifra = {}
        for i in range(C):
            mapa_cifra[cifra1[i]] = cifra2[i]
            mapa_cifra[cifra1[i].lower()] = cifra2[i].lower()
            mapa_cifra[cifra2[i]] = cifra1[i]
            mapa_cifra[cifra2[i].lower()] = cifra1[i].lower()

        resultados = []

        for _ in range(N):
            frase = input()
            nova_frase = ''.join(mapa_cifra.get(letra, letra) for letra in frase)
            resultados.append(nova_frase)

        print('\n'.join(resultados))
        print()

    except EOFError:
        break
