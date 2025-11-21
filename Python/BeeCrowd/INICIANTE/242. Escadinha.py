N = int(input())
dados = list(map(int, input().split()))
escadinhas = 0

if len(dados) == 1:
    print(1)
else:
    while len(dados) >= 2:
        if len(dados) > 1 and dados[0] == dados[1]:
            while len(dados) > 1 and dados[0] == dados[1]:
                dados.pop(0)
            escadinhas += 1
        else:
            x = dados[1] - dados[0]
            contador = 0
            try:
                while len(dados) > 1 and dados[1] - dados[0] == x:
                    dados.pop(0)
                escadinhas += 1
            except IndexError:
                escadinhas += 1
                break

    print(escadinhas)
