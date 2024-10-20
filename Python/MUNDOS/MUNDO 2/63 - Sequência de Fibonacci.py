x = int(input("Quantos elementos deseja ver da Sequência de Fibonacci?: "))
numAtual = 0
numAntigo = 0
valor = 0
i = 1


while i <= x:
    print("{}º Termo: {}, ".format(i, numAtual))
    if numAtual == 0:
        numAtual = 1
        numAntigo = 0
    else:
        valor = numAtual
        numAtual = numAtual + numAntigo
        numAntigo = valor
    i += 1
