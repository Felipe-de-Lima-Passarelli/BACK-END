from time import sleep


def notas(*notas, sit = False):
    biblioteca = dict()
    contagem = 0
    maior = 0
    menor = 0
    somanum = 0
    for i, n in enumerate(notas):
        if i == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        contagem += 1
        somanum += n

    biblioteca["Total"] = contagem
    biblioteca["Maior"] = maior
    biblioteca["Menor"] = menor
    biblioteca["Média"] = (somanum/contagem)

    if sit:
        if biblioteca["Média"] >= 7:
            biblioteca["Situação"] = "Boa"
        elif biblioteca["Média"] >= 5:
            biblioteca["Situação"] = "Razoável"
        else:
            biblioteca["Situação"] = "Ruim"
    return biblioteca

resp1 = notas(10, 8, 6, 8, sit = True)
resp2 = notas(7, 8, 7, 5, sit = True)
resp3 = notas(7, 2, 4, 5, sit = True)
print(resp1)
sleep(2)
print(resp2)
sleep(2)
print(resp3)
