soma = 0
for c in range(0,6):
    x = int(input("Digite um número inteiro positivo"))
    if x%2 == 0:
        soma += x

if soma == 0:
    print("Não houve nenhum número par para ser somado")
else:
    print("A soma dos números pares deu: {}".format(soma))
