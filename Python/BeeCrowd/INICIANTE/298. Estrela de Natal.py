N = int(input())
ano_Atual = 2020
ano_Final = 2020 + N

ano_Atual += 1
contador = 0

while ano_Atual <= ano_Final:
    if ano_Atual % 4 == 0:
        if ano_Atual % 100 == 0:
            if ano_Atual % 400 == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False
    if is_leap:
        contador += 1
    ano_Atual += 1

dias_terra = (365 * N) + contador
dias_jupiter = dias_terra * 11.9
dias_saturno = dias_terra * 29.6

print(dias_jupiter)
print(dias_saturno)
