alfabeto = "abcdefghijklmnopqrstuvwxyz"

K = str(input())
N = int(input())
vogal = ["a", "e", "i", "o", "u"]

for _ in range(0, N):
    i = 0
    frase = list(map(str, input().split()))
    fraseinicial = ""
    for palavras in frase:
        if palavras != frase[-1]:
            fraseinicial += palavras + " "
        else:
            fraseinicial += palavras

    frasefinal = ""
    for palavras in frase:
        if palavras[0] in vogal:
            frasefinal += palavras + " "
        else:
            novapalavra = ""
            while len(novapalavra) != len(palavras):
                novapalavra += K[i]
                i += 1
                if i == len(K):
                    i = 0
            frasefinal += novapalavra + " "
    frasefinal = frasefinal.rstrip()
    fraseinicial = fraseinicial.split(" ")
    frasefinal = frasefinal.split(" ")
    respostafinal = ""

    for i in range(0, len(fraseinicial)):
        if i != (len(fraseinicial) - 1):
            if fraseinicial[i] == frasefinal[i]:
                respostafinal += fraseinicial[i] + " "
            else:
                c = 0
                for letras in frasefinal[i]:
                    posicao = alfabeto.index(letras)
                    posicao += alfabeto.index(fraseinicial[i][c])
                    if posicao > 25:
                        posicao -= 26
                    respostafinal += alfabeto[posicao]
                    c += 1
                respostafinal = respostafinal + " "
        else:
            if fraseinicial[i] == frasefinal[i]:
                respostafinal += fraseinicial[i]
            else:
                c = 0
                for letras in frasefinal[i]:
                    posicao = alfabeto.index(letras)
                    posicao += alfabeto.index(fraseinicial[i][c])
                    if posicao > 25:
                        posicao -= 26
                    respostafinal += alfabeto[posicao]
                    c += 1

    print(respostafinal)
