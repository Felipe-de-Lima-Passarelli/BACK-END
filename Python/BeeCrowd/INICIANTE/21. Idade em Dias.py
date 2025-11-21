#ano = 365 dias
#mês = 30 dias

idade = int(input()) #Idade em dias

ano = 0
mes = 0
dia = 0

while idade >= 365:
    ano += 1
    idade -= 365

while idade >= 30:
    mes += 1
    idade -= 30

while idade >= 1:
    dia += 1
    idade -= 1

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
