a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = (b**2) - (4*a*c)

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    x1 = ((-b) + (delta ** (1 / 2))) / (2 * a)
    x2 = ((-b) - (delta ** (1 / 2))) / (2 * a)
    print("A equação fornecida terá raízes {:.2f} e {:.2f}".format(x1, x2))
