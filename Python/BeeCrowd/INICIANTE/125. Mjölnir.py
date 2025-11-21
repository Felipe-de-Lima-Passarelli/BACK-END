C = int(input())

for i in range(0, C):
    nome, forca = input().split()
    nome = str(nome)
    forca = int(forca)

    while forca < 0 or forca > 25000:
        nome, forca = input().split()
        nome = str(nome)
        forca = int(forca)

    if nome != "Thor":
        print("N")
    else:
        print("Y")
