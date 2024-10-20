from time import sleep
while True:
    valor = int(input("Digite o número que deseja saber a tabuada: "))
    i = 1
    while i <= 10:
        print(f"{valor} x {i} = {valor * i}")
        i += 1
    sleep(2)
    x = int(input('''Escolha uma opção
    [0] - Desejo finalizar o programa
    [1] - Desejo continuar o programa '''))
    if x == 0:
        break
    elif x == 1:
        valor = int(input("Digite o número que deseja saber a tabuada: "))
        i = 1
        while i <= 10:
            print(f"{valor} x {i} = {valor*i}")
            i += 1
        sleep(1)
        x = int(input('''Escolha uma opção
        [0] - Desejo finalizar o programa
        [1] - Desejo continuar o programa '''))
        if x == 0:
            break
    else:
        sleep(1)
        print("Você digitou um valor inválido, tente novamente")
        x = int(input('''Escolha uma opção
        [0] - Desejo finalizar o programa
        [1] - Desejo continuar o programa '''))
        sleep(1)
sleep(0.5)
print("-=-=-=-=-= Fim do Programa -=-=-=-=-=")
