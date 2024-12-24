from time import sleep
a = float(input("Digite o valor do primeiro lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

print("---------- Analisando se é possível fazer um triângulo com os lados informados por você ----------")
sleep(5)

if a < (b+c) and b < (a+c) and c < (a+b):
    print("É possível fazer um triângulo com esses lados")

    if a == b and b == c:
        print("É um triângulo Equilátero, pois todos lados são iguais")
    elif a == b or b == c or a == c:
        print("É um triângulo Isósceles, pois existem dois lados iguais")
    else:
        print("É um triângulo Escaleno, pois todos lados são diferentes")
else:
    print("Não é possível fazer um triângulo com esses lados")
