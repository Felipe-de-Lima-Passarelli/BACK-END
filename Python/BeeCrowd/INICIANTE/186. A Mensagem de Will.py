while True:
    try:
        alfabeto = str(input())
        N = int(input())
        lampadas = list(map(int, input().split()))
        while len(lampadas) != N:
            lampadas = list(map(int, input().split()))

        mensagem = ""
        for numeros in lampadas:
            mensagem += alfabeto[numeros - 1]

        print(mensagem)

    except EOFError:
        break
