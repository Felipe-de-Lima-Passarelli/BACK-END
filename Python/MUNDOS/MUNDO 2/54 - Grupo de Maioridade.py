from datetime import date, datetime
ano = date.today().year
maioridade = 0
menoridade = 0

for i in range (0, 7):
    nascimento = int(input("Digite o ano de seu nascimento: "))
    idade = ano - nascimento
    if idade < 21:
        menoridade += 1
    else:
        maioridade += 1
print("{} pessoas ainda não atingiram a maior idade".format(menoridade))
print("{} pessoas já atingiram a maior idade".format(maioridade))
