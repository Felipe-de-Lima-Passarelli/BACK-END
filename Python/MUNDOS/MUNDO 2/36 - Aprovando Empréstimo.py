valorCasa = float(input("Digite o valor em R$ da casa: "))
salario = float(input("Digite o valor do seu salário em R$: "))
ano = int(input("Digite em quantos anos você vai pagar a casa"))

mes = (ano * 12)

if (valorCasa/mes) > (0.3*salario):
    print("Empréstimo negado")
else:
    print("Você pode fazer o empréstimo!")
