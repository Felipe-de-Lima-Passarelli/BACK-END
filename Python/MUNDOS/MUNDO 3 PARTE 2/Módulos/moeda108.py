def metade(num = 0):
    x = (num/2)
    return x

def dobro(num = 0):
    x = num*2
    return x

def aumentar(num = 0, porc = 0):
    x = (num*(1 + (porc/100)))
    return x

def diminuir(num = 0, porc = 0):
    x = (num * (1 - (porc / 100)))
    return x

def moeda(preco = 0, simbolo = "R$"):
    return f"{simbolo}{preco:.2f}".replace(".", ",")
