par = []
impar = []

for i in range(0, 15):
    X = int(input())
    if X%2 == 0:
        par.append(X)
    else:
        impar.append(X)

    if len(par) == 5:
        for numpar in range(0, 5):
            print(f"par[{numpar}] = {par[numpar]}")
        par = []

    if len(impar) == 5:
        for numimpar in range(0, 5):
            print(f"impar[{numimpar}] = {impar[numimpar]}")
        impar = []

for posicaoimpar, numeroimpar in enumerate(impar):
    print(f"impar[{posicaoimpar}] = {numeroimpar}")

for posicaopar, numeropar in enumerate(par):
    print(f"par[{posicaopar}] = {numeropar}")
