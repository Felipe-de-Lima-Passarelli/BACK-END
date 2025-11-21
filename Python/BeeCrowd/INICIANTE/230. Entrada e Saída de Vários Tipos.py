dados = input().split()
num1 = int(dados[0])
num2 = float(dados[1])
letra = str(dados[2])
frase = " ".join(dados[3:])

print(f"{num1}{num2}{letra}{frase}")
print(f"{num1}\t{num2}\t{letra}\t{frase}")
print(f"{num1:>10}{num2:>10}{letra:>10}{frase:>10}")
