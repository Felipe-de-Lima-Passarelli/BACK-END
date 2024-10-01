x = int(input("Digite um ano aleatório e eu direi se é bissexto ou não: "))

if x%4 == 0 and x%100 != 0:
    print("É um ano bissexto")
else:
    if x%100 == 0 and x%400 == 0:
        print("É um ano bissexto")
    else:
        print("Não é um ano bissexto")
