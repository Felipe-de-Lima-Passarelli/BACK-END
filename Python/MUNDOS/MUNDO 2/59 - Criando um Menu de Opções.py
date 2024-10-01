from time import sleep

num1 = float(input("Digite o primeiro número desejado: "))
num2 = float(input("Digite o segundo número desejado: "))

escolha = int(input((''''Escolha a operação matemática que deseja:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa ''')))

while escolha != 5:
    if escolha == 1:
        print("A soma entre {} e {} é: {}".format(num1, num2, (num1+num2)))
        sleep(2)
        num1 = float(input("Digite o primeiro número desejado: "))
        num2 = float(input("Digite o segundo número desejado: "))
        escolha = int(input((''''Escolha a operação matemática que deseja:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa ''')))
    elif escolha == 2:
        print("A multiplicação entre {} e {} é: {}".format(num1, num2, (num1*num2)))
        sleep(2)
        num1 = float(input("Digite o primeiro número desejado: "))
        num2 = float(input("Digite o segundo número desejado: "))
        escolha = int(input((''''Escolha a operação matemática que deseja:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa ''')))
    elif escolha == 3:
        if num1 > num2:
            print("O maior número entre {} e {} é: {}".format(num1, num2, num1))
            sleep(2)
            num1 = float(input("Digite o primeiro número desejado: "))
            num2 = float(input("Digite o segundo número desejado: "))
            escolha = int(input((''''Escolha a operação matemática que deseja:
            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos Números
            [5] Sair do programa ''')))
        else:
            print("O maior número entre {} e {} é: {}".format(num1, num2, num2))
            sleep(2)
            num1 = float(input("Digite o primeiro número desejado: "))
            num2 = float(input("Digite o segundo número desejado: "))
            escolha = int(input((''''Escolha a operação matemática que deseja:
            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos Números
            [5] Sair do programa ''')))
    elif escolha == 4:
        print("Você quer digitar novos números? Tudo bem, aguarde 2 segundos!")
        sleep(2)
        num1 = float(input("Digite o primeiro número desejado: "))
        num2 = float(input("Digite o segundo número desejado: "))
        escolha = int(input((''''Escolha a operação matemática que deseja:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa ''')))
    else:
        print("Digite um número válido para sua escolha")
        sleep(2)
        num1 = float(input("Digite o primeiro número desejado: "))
        num2 = float(input("Digite o segundo número desejado: "))
        escolha = int(input((''''Escolha a operação matemática que deseja:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa ''')))

print("Fim do Programa!")
