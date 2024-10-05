from time import sleep
from functools import reduce

numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x**2, numeros))
print(f"O quadrado dos números da lista são: {quadrados}")

sleep(1)

pares = list(filter(lambda x: x%2 == 0, numeros))
print(f"Os números pares são: {pares}")

sleep(1)

soma_total = reduce(lambda x, y: x + y, numeros)
print(f"A soma de todos valores da lista deu: {soma_total}")
