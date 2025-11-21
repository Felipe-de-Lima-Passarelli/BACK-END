N, C , M = map(int, input().split())

contador = C
figurascarimbadas = list(map(int, input().split()))
figurascompradas = list(map(int, input().split()))

for numeros in figurascarimbadas:
    if numeros in figurascompradas:
        contador -= 1

print(contador)
