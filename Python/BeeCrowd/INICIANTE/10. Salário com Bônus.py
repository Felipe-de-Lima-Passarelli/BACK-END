nome = str(input())
salario = round(float(input()), 2)
vendas = round(float(input()), 2)

salariofinal = salario + (vendas*0.15)
print(f"TOTAL = R$ {salariofinal:.2f}")
