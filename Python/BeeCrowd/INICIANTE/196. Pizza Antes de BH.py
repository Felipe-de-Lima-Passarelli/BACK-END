while True:
    try:
        N, D = map(int, input().split())

        datas = []
        pessoas = []
        for _ in range(0, D):
            dados = input().split()
            datas.append(str(dados[0]))
            dados.pop(0)
            pessoas.append(list(map(int, dados)))

        dataresposta = ""
        contador = 0
        for numeros in pessoas:
            if dataresposta == "":
                if numeros.count(1) == N:
                    dataresposta = datas[contador]
                contador += 1

        if dataresposta == "":
            print("Pizza antes de FdI")
        else:
            print(dataresposta)

    except EOFError:
        break
