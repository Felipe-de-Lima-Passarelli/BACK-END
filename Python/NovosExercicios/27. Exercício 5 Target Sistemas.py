entrada = input("Digite uma palavra: ").lower()
entrada_invertida = ""

for i in range((len(entrada) - 1), -1, -1):
    entrada_invertida += entrada[i]

print(entrada_invertida)
