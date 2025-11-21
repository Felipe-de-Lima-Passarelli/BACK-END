while True:
    entrada = input().split()
    if len(entrada) == 1 and entrada[0] == "0":
        break

    if len(entrada) == 3:
        A, B, C = map(int, entrada)

    area = A*B
    areaterreno = area/(C/100)
    ladoterreno = int((areaterreno**(1/2)))
    print(ladoterreno)
