a = float(input("Digite o comprimento de A"))
b = float(input("Digite o comprimento de B"))
c = float(input("Digite o comprimento de C"))

teste1 = float(b - c)
teste2 = float(b + c)
teste3 = float(a - c)
teste4 = float(a + c)
teste5 = float(b - a)
teste6 = float(b + a)


if a < 0 or b < 0 or c < 0:
    print("Digite valores positivos")
else:
    if a > teste1 and a < teste2:
        print("É um triângulo")
    else:
        if b > teste3 and b < teste4:
            print("É um triângulo")
        else:
            if c > teste5 and c < teste6:
                print("É um triângulo")
            else:
                print("Não é um triângulo")
