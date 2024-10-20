x = int(input("Digite um número inteiro positivo para analisar se é primo ou não"))
primo = 0

if x < 1:
    print("Digite um número inteiro positivo")
    breakpoint()
elif x == 1:
    print("O número {} não é um número primo".format(x))
    breakpoint()
else:
    for c in range(1, (x + 1)):
        if x%c == 0:
            primo = primo + 1

if primo == 2:
    print("O número {} é um número primo".format(x))
else:
    print("O número {} não é um número primo".format(x))
