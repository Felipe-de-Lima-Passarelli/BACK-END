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
