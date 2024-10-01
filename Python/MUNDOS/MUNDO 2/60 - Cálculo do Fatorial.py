x = int(input("Digite um número inteiro positivo para calcular seu fatorial"))
i = 1
valor = 1

if x <= 0:
    print("Valor Inválido")
else:
    print("A soma de {} fatorial é: ".format(x), end = "")
    while x > i:
        print("{} * ".format(x), end = "")
        valor *= x
        x -= 1
    while x == i:
        print("{} = ".format(x), end="")
        x -= 1
    print(valor)
