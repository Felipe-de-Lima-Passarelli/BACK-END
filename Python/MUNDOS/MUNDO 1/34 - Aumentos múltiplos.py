salario = float(input("Digite seu salário"))

if salario > 1250:
    salario = (salario * 1.10)
    print("Seu novo salário será aumentado em 10%, o valor novo é: {}".format(salario))
else:
    salario = (salario * 1.15)
    print("Seu novo salário será aumentado em 15%, o valor novo é: {}".format(salario))
