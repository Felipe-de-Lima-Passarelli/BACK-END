salario = round(float(input()), 2)
novosalario = 0
reajuste = 0
porcentagem = 0

if salario <= 400:
    novosalario = salario * 1.15
    reajuste = salario*0.15
    porcentagem = 15
elif salario <= 800:
    novosalario = salario * 1.12
    reajuste = salario * 0.12
    porcentagem = 12
elif salario <= 1200:
    novosalario = salario * 1.10
    reajuste = salario * 0.10
    porcentagem = 10
elif salario <= 2000:
    novosalario = salario * 1.07
    reajuste = salario * 0.07
    porcentagem = 7
else:
    novosalario = salario * 1.04
    reajuste = salario * 0.04
    porcentagem = 4

print(f"Novo salario: {novosalario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {porcentagem} %")
