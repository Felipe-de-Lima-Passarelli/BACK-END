from functools import reduce

lista = [-50, -42, -32, -12, -5, -1, 0 ,1, 5, 9, 13, 15, 23, 29, 32, 40]
soma_total = reduce(lambda x, y: x + y, lista)
print(f"A soma dos números da lista deu: {soma_total}")
