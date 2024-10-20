from random import choice
from time import sleep
print("-=-=-=-=-= Olá, vamos jogar ímpar ou par? -=-=-=-=-=")
sleep(1)
contagem = 0
while True:
    computador = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    escolhaComputador = choice(computador)
    escolha = int(input('''Escolha uma opção
    [1] Ímpar
    [2] Par'''))

    if escolha == 1:
        num = int(input("Digite seu número, entre 0 a 10: "))
        while num < 0 or num > 10:
            print("Número inválido, digite novamente")
            num = int(input("Digite seu número, entre 0 a 10: "))
        if (num + escolhaComputador)%2 != 0:
            contagem += 1
            print(f"Você venceu, eu escolhi {escolhaComputador} e você escolheu {num}")
            sleep(1)
            print("Vamos novamente")
            sleep(1)
        else:
            print(f"Você perdeu, eu escolhi {escolhaComputador} e você escolheu {num}")
            break

    elif escolha == 2:
        num = int(input("Digite seu número, entre 0 a 10: "))
        while num < 0 or num > 10:
            print("Número inválido, digite novamente")
            num = int(input("Digite seu número, entre 0 a 10: "))
        if (num + escolhaComputador) % 2 == 0:
            contagem += 1
            print(f"Você venceu, eu escolhi {escolhaComputador} e você escolheu {num}")
            sleep(1)
            print("Vamos novamente")
            sleep(1)
        else:
            print(f"Você perdeu, eu escolhi {escolhaComputador} e você escolheu {num}")
            break
    else:
        print("Opção Inválida, digite novamente")
        escolha = int(input('''Escolha uma opção
        [1] Ímpar
        [2] Par'''))

if contagem == 0:
    sleep(1)
    print(f"Você não conseguiu vencer nenhuma vez")
elif contagem == 1:
    sleep(1)
    print("Você venceu apenas uma vez")
else:
    sleep(1)
    print(f"Você venceu {contagem} vezes consecutivas")
