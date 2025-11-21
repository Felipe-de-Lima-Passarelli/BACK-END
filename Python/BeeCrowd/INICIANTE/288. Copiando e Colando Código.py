while True:
    try:
        entradas = []
        while True:
            x = str(input())
            entradas.append(x)
            if x == "</html>":
                break

        posicao_inicial = entradas.index("    <body>")
        posicao_final = entradas.index("    </body>")

        for i in range((posicao_inicial + 1), posicao_final):
            print(entradas[i])

    except EOFError:
        break
