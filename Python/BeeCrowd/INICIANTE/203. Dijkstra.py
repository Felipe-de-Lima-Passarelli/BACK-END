joias = []

try:
    while True:
        frase = str(input())
        if not frase in joias:
            joias.append(frase)
except EOFError:
    pass

print(len(joias))
