num1 = int(input("Digite um valor positivo inteiro"))
num2 = int(input("Digite outro valor positivo inteiro"))

if num1 == num2:
    print("Não existe valor maior entre {} e {}, pois os dois são iguais".format(num1, num2))
elif num1 > num2:
    print("O maior valor entre {} e {} é: {}".format(num1, num2, num1))
else:
    print("O maior valor entre {} e {} é: {}".format(num1, num2, num2))
