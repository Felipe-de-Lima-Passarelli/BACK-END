def fatorial(x):
    num1 = 0
    num2 = 1
    lista = []
    for i in range(0, x):
        if i == 0:
            lista.append(num1)
        elif i == 1:
            lista.append(num2)
        else:
            lista.append(num1 + num2)
            num1, num2 = num2, (num1 + num2)
    return lista

T = int(input())

for _ in range(0, T):
    numero = str(input())
    print(f"{fatorial(int(numero, 2) + 1)[-1]:03d}")
