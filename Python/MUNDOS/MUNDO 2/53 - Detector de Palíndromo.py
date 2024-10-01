frase = str(input("Digite uma frase para analisar se é palíndromo ou não: "))
frase = frase.strip().lower().replace(" ", "")

if frase == frase[::-1]:
    print("Essa frase é um palíndromo")
else:
    print("Essa frase não é um palíndromo")
