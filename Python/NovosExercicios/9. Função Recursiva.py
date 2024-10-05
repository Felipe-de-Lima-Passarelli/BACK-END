from functools import reduce

lista = [1, 2, 3, 4]

def soma(numeros):
    soma_total = reduce(lambda x, y: x + y, numeros)
    print(soma_total)

soma(lista)
soma([2, 5, 9])
