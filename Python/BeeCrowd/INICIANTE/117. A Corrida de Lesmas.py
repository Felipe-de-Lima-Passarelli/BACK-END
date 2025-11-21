while True:
    try:
        L = int(input())
    except EOFError:
        break

    while L < 1 or L > 500:
        L = int(input())


    dados = input().split()
    while len(dados) != L:
        dados = input().split()

    listavelocidade = []
    for i in range(0, L):
        listavelocidade.append(int(dados[i]))

    if int(max(listavelocidade)) < 10:
        print(1)
    elif int(max(listavelocidade)) < 20:
        print(2)
    else:
        print(3)
