respostas = {
    "esquerda": "ingles",
    "direita": "frances",
    "nenhuma": "portugues",
    "as duas": "caiu"
}

while True:
    try:
        frase = str(input())
        print(respostas[frase])

    except EOFError:
        break
