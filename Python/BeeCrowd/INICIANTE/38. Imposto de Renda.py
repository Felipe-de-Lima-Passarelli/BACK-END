salario = round(float(input()), 2)

if salario <= 2000.00:
    print("Isento")
elif salario <= 3000.00:
    imposto1 = salario - 2000.00
    taxa1 = (imposto1 * 0.08)
    print(f"R$ {taxa1:.2f}")
elif salario <= 4500.00:
    imposto1 = salario - 3000.00
    taxa1 = (imposto1 * 0.18)
    taxa2 = 1000 * 0.08
    impostototal = taxa1 + taxa2
    print(f"R$ {impostototal:.2f}")
else:
    imposto1 = salario - 4500.01
    taxa1 = (imposto1 * 0.28)
    taxa2 = 1500 * 0.18
    taxa3 = 1000 * 0.08
    impostototal = taxa1 + taxa2 + taxa3
    print(f"R$ {impostototal:.2f}")
