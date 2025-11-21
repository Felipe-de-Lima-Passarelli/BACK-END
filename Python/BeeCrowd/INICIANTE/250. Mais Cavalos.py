alfabeto = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
}

entrada, saida = map(str, input().split())
resposta = "INVALIDO"
posicao = [alfabeto[entrada[0]] - 2 ,alfabeto[entrada[0]] - 1 ,alfabeto[entrada[0]] + 1, alfabeto[entrada[0]] + 2]

if alfabeto[saida[0]] in posicao:
    if alfabeto[entrada[0]] - alfabeto[saida[0]] == 1:
        if int(saida[1]) + 2 == int(entrada[1]) or int(saida[1]) - 2 == int(entrada[1]):
            resposta = "VALIDO"
    elif alfabeto[entrada[0]] - alfabeto[saida[0]] == 2:
        if int(saida[1]) + 1 == int(entrada[1]) or int(saida[1]) - 1 == int(entrada[1]):
            resposta = "VALIDO"

print(resposta)
