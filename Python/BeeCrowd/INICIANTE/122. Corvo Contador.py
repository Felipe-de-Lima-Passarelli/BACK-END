resultados = []
soma_atual = 0

piscadas = {
    '---': 0,
    '--*': 1,
    '-*-': 2,
    '-**': 3,
    '*--': 4,
    '*-*': 5,
    '**-': 6,
    '***': 7
}

while len(resultados) < 3:
    entrada = input()

    if entrada == 'caw caw':
        print(soma_atual)
        resultados.append(soma_atual)
        soma_atual = 0
    else:
        soma_atual += piscadas[entrada]
