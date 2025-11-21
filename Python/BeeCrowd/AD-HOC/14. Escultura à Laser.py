while True:
    A, C = map(int, input().split())
    if A == 0 and C == 0:
        break

    altura_atual_das_colunas = []
    altura_final_das_colunas = list(map(int, input().split()))
    for _ in range(0, len(altura_final_das_colunas)):
        altura_atual_das_colunas.append(A)

    contagem_laser = 0
    laser = False

    while altura_atual_das_colunas != altura_final_das_colunas:
        for i in range(0, len(altura_atual_das_colunas)):
            if altura_atual_das_colunas[i] > altura_final_das_colunas[i]:
                if laser:
                    altura_atual_das_colunas[i] -= 1
                else:
                    laser = True
                    altura_atual_das_colunas[i] -= 1
                    contagem_laser += 1
            else:
                if laser:
                    laser = False
        laser = False

    print(contagem_laser)
