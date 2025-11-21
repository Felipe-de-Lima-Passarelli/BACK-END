QT = int(input())
while QT < 1 or QT > 100:
    QT = int(input())

for i in range(0, QT):
    nome1, escolha1, nome2, escolha2 = input().split()
    nome1 = str(nome1)
    escolha1 = str(escolha1)
    nome2 = str(nome2)
    escolha2 = str(escolha2)

    numero1, numero2 = input().split()
    numero1 = int(numero1)
    numero2 = int(numero2)

    if (numero1 + numero2)%2 == 0:
        if escolha1 == "PAR":
            print(nome1)
        else:
            print(nome2)
    else:
        if escolha1 == "IMPAR":
            print(nome1)
        else:
            print(nome2)
