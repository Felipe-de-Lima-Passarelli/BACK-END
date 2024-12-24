from time import sleep

lista = []

while True:
    x = int(input("Digite um número inteiro positivo: "))
    while x <= 0:
        print("Número Inválido")
        sleep(1)
        x = int(input("Digite um número inteiro positivo: "))
    lista.append(x)
    escolha = int(input('''Deseja continuar cadastrando números novos?
    [0] - Não
    [1] - Sim'''))
    if escolha == 0:
        break

lista.sort(reverse = True)
print(f"Foram digitados {len(lista)} números")
print(f"A lista em ordem decrescente ficou assim: {lista}")

if 5 in lista:
    print("O valor 5 foi digitado na lista")
else:
    print("O valor 5 não foi digitado na lista")
