soma = 0
contagem = 0
while True:
    x = int(input("Digite um número inteiro positivo"))
    if x == 999:
        break
    soma += x
    contagem += 1
print(f"Você digitou {contagem} números, e a soma entre eles deu um total de {soma}")
