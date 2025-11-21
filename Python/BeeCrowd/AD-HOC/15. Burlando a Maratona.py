from fractions import Fraction

N = int(input())

for _ in range(0, N):
    dados = list(input().split())
    lado_esquerdo = ""
    lado_direito = ""
    operador = ""
    for caracteres in dados:
        if caracteres == "+" or caracteres == "-" or caracteres == "*" or (caracteres == "/" and lado_esquerdo.count("/") == 1):
            operador = caracteres
            break
        else:
            lado_esquerdo += caracteres
    for _ in range(0, len(lado_esquerdo) + 1):
        dados.pop(0)
    for resto in dados:
        lado_direito += resto

    if operador == "+":
        resultado = eval(lado_esquerdo) + eval(lado_direito)
    elif operador == "-":
        resultado = eval(lado_esquerdo) - eval(lado_direito)
    elif operador == "*":
        resultado = eval(lado_esquerdo) * eval(lado_direito)
    else:
        resultado = eval(lado_esquerdo) / eval(lado_direito)

    fracao = Fraction(resultado).limit_denominator(100)
    num = int((int(lado_esquerdo[-1]) * int(lado_direito[-1])) / fracao.denominator)
    fracao_inicial = fracao.numerator * num, fracao.denominator * num

    print(f"{int(fracao_inicial[0])}/{int(fracao_inicial[1])} = {fracao}")
