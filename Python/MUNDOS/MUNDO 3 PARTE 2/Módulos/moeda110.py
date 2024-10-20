def metade(num = 0, form = False):
    x = (num/2)
    if not form:
        return x
    else:
        return moeda(x)

def dobro(num = 0, form = False):
    x = num*2
    if not form:
        return x
    else:
        return moeda(x)

def aumentar(num = 0, porc = 0, form = False):
    x = (num*(1 + (porc/100)))
    if not form:
        return x
    else:
        return moeda(x)

def diminuir(num = 0, porc = 0, form = False):
    x = (num * (1 - (porc / 100)))
    if not form:
        return x
    else:
        return moeda(x)

def moeda(preco = 0, simbolo = "R$"):
        return f"{simbolo}{preco:.2f}".replace(".", ",")

def resumo(preco = 0, aumento = 10, reducao = 5):
    print(30*"-=")
    print("               RESUMO DO VALOR")
    print(30 * "-=")
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, form = True)}")
    print(f"Metade do preço: \t{metade(preco, form = True)}")
    print(f"20% de aumento: \t{aumentar(preco, aumento, form = True)}")
    print(f"12% de redução: \t{diminuir(preco, reducao, form = True)}")
