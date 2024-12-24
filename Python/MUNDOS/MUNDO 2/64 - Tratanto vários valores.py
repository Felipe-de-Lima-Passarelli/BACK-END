from time import sleep
x = int(input("Digite um número inteiro positivo: "))
soma = 0
contagem = 0

if x <= 0:
    print("Número inválido, digite um número inteiro positivo da próxima vez")
else:
    while x != 999:
        soma += x
        contagem += 1
        sleep(1)
        x = int(input("Digite outro número inteiro positivo: "))
        print("Caso queira parar de digitar números, digite 999")
        sleep(1)
print("Fim do programa, você digitou {} números. A soma de todos deu um total de : {}".format(contagem, soma))
