numeros = range(1, 6)
novalista = list(map(lambda x: f"\nNúmero: {x}", numeros))
print(*novalista, sep = "\n")
