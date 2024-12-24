from time import sleep
lista = []

while True:
    x = int(input("Digite um valor inteiro positivo: "))
    while x <= 0:
        print("Número Inválido")
        sleep(1)
        x = int(input("Digite um valor inteiro positivo: "))
    if x in lista:
        print("Esse número já foi cadastrado")
        sleep(1)
    else:
        lista.append(x)
    sleep(1)
    escolha = int(input('''Deseja continuar adicionando numeros?
    [0] - Não
    [1] - Sim'''))
    if escolha == 0:
        break

lista.sort()
print(lista)
