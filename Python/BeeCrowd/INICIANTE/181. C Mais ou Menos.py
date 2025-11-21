while True:
    T = int(input())
    if T == 0:
        break

    totalmg = 0

    for i in range(0, T):
        nome = ""
        dados = input().split()
        quantidade = int(dados[0])
        dados.pop(0)
        for nomes in dados:
            if nomes != dados[len(dados) - 1]:
                nome += nomes + " "
            else:
                nome += nomes

        if nome == "suco de laranja":
            totalmg += 120 * quantidade
        if nome == "morango fresco":
            totalmg += 85 * quantidade
        if nome == "mamao":
            totalmg += 85 * quantidade
        if nome == "goiaba vermelha":
            totalmg += 70 * quantidade
        if nome == "manga":
            totalmg += 56 * quantidade
        if nome == "laranja":
            totalmg += 50 * quantidade
        if nome == "brocolis":
            totalmg += 34 * quantidade

    if totalmg > 130:
        print(f"Menos {totalmg - 130} mg")
    elif totalmg < 110:
        print(f"Mais {110 - totalmg} mg")
    else:
        print(f"{totalmg} mg")
