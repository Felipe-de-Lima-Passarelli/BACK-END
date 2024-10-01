x = int(input("Digite um número inteiro positivo: "))

if x < 1:
    print("Digite um valor inteiro positivo")
else:
    if x%2 == 0:
        print("Seu número {} é par".format(x))
    else:
        print("Seu número {} é ímpar".format(x))
