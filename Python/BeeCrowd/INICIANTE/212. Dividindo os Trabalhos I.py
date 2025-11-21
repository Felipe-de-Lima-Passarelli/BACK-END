while True:
    try:
        N = int(input())
        dados = list(map(int, input().split()))
        total = sum(dados)
        soma = 0
        testeacima = 0
        testeabaixo = 0

        for i in range(0, len(dados)):
            soma += dados[i]
            if soma >= total//2:
                testeacima = soma + dados[i + 1]
                testeabaixo = soma - dados[i]
                break

        resposta = [abs(soma - (total - soma)), abs(testeacima - (total - testeacima)), (abs(testeabaixo - (total - testeabaixo)))]
        print(min(resposta))

    except EOFError:
        break
