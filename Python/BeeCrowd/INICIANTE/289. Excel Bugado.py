alfabeto = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
verificacao = ["A", "B", "C", "D"]

while True:
    try:
        S = str(input())
        contador = 0
        if len(S) == 1:
            contador += alfabeto.index(S[0])
            print(contador)
        elif len(S) == 2:
            contador += 26
            contador += alfabeto.index(S[1])
            print(contador)
        elif len(S) == 3:
            if S[2] not in verificacao:
                print("Essa coluna nao existe Tobias!")
            else:
                contador += 52
                contador += alfabeto.index((S[2]))
                print(contador)
        else:
            print("Essa coluna nao existe Tobias!")

    except EOFError:
        break
