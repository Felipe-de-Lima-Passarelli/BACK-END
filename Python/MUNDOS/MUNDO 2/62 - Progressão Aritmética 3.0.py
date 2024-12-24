from time import sleep

num = int(input("Digite o primeiro termo da P.A de 10 termos: "))
razao = int(input("Digite a razão da P.A: "))
i = 1
n = 0

while i <= 10:
    print("{}º Termo: {}, ".format(i, num))
    num = (num + razao)
    i += 1

escolha = int(input('''Deseja mostrar mais alguns termos?
[0] - Não
[1] - Sim '''))

if escolha != 0 and escolha != 1:
    print("Digite um número válido. Aguarde 2 segundos, por favor")
    sleep(2)
    escolha = int(input('''Deseja mostrar mais alguns termos?
    [0] - Não
    [1] - Sim '''))
elif escolha == 1:
    i = 1
    n = int(input("Quantos mais termos deseja ver?"))
    while i <= n:
        print("{}º Termo: {}, ".format((10 + i), num))
        num = (num + razao)
        i += 1
else:
    print("Fim da P.A")
