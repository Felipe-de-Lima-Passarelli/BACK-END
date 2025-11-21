N = int(input())
while N < 0 or N > 34:
    N = int(input())

frase = "LIFE IS NOT A PROBLEM TO BE SOLVED"

resultado = ""
for i in range(0, N):
    resultado += frase[i]

print(resultado)
