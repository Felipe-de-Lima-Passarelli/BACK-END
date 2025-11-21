N = int(input())
matriz = []
respostafinal = 0

for _ in range(0, N):
    linha = []
    numeros = list(map(int, input().split()))
    for n in numeros:
        linha.append(n)
    matriz.append(linha)

numerosnecessarios = 0

for linha in range(0, N):
    numerosnecessarios += 1
    posicao_obrigatoria_anterior = []
    numeros_usados = []
    if linha == 0:
        while len(numeros_usados) != numerosnecessarios:
            menor = 9999
            for i in range(0, N):
                if matriz[linha][i] < menor:
                    menor = matriz[linha][i]
                    pos = i
            numeros_usados.append(menor)
            posicao_obrigatoria_anterior.append(pos)
            matriz[linha][pos] = 9999
        respostafinal += sum(numeros_usados)
    else:
        for posicoes in posicao_obrigatoria_anterior:
            numeros_usados.append(matriz[linha][posicoes])
        while len(numeros_usados) != numerosnecessarios:
            menor = 9999
            for i in range(0, N):
                if i not in posicao_obrigatoria_anterior:
                    if matriz[linha][i] < menor:
                        menor = matriz[linha][i]
                        pos = i
            numeros_usados.append(menor)
            posicao_obrigatoria_anterior.append(pos)
            matriz[linha][pos] = 9999
            if menor == 9999:
                break
        respostafinal += sum(numeros_usados)

print(respostafinal)
