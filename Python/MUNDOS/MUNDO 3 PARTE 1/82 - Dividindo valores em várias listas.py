from time import sleep

listatotal = []
listapar = []
listaimpar = []

while True:
    x = int(input("Digite um número inteiro positivo: "))
    while x <= 0:
        print("Número Inválido")
        sleep(1)
        x = int(input("Digite um número inteiro positivo: "))
    listatotal.append(x)
    if x %2 == 0:
        listapar.append(x)
    else:
        listaimpar.append(x)
    escolha = int(input('''Deseja continuar cadastrando números novos?
    [0] - Não
    [1] - Sim'''))
    if escolha == 0:
        break

print(f"Lista total foi: {listatotal}")
print(f"Lista dos Pares: {listapar}")
print(f"Lista do Ímpares: {listaimpar}")
