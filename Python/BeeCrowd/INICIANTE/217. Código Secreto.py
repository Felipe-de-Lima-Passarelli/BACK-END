alfabeto = {
    "": "abc",
    " ": "def",
    "  ": "ghi",
    "   ": "jkl",
    "    ": "mno",
    "     ": "pqr",
    "      ": "stu",
    "       ": "vwx",
    "        ": "yz"
}

while True:
    try:
        N = int(input())

        for _ in range(0, N):
            biblioteca = ""
            resposta = str(input())
            espacos = resposta.count(" ")
            respostafinal = ""
            respostafora = ""
            for letras in resposta:
                if respostafora.count(" ") == espacos:
                    respostafinal += letras
                else:
                    respostafora += letras
            pontos = respostafinal.count(".")

            if espacos == 0:
                print(alfabeto[""][pontos - 1])
            else:
                total = ""
                for _ in range(0, espacos):
                    total += " "
                print(alfabeto[total][pontos - 1])

    except EOFError:
        break
