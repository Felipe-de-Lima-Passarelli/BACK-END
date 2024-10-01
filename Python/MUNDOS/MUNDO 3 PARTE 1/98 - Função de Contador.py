from time import sleep


def contador(inicio, fim, passo):
    print(f"\nContagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        for i in range(inicio, (fim + 1), passo):
            print(i, end = " ")
            sleep(0.5)
    elif inicio > fim:
        if passo > 0:
            for i in range(inicio, (fim - 1), -passo):
                print(i, end = " ")
                sleep(0.5)
        else:
            for i in range(inicio, (fim - 1), passo):
                print(i, end = " ")
                sleep(0.5)

contador(1, 10, 1)
contador(10, 0, 2)

print("\nAgora é sua vez de personalizar a contagem!")
a = int(input("Início: "))
b = int(input("Fim: "))
c = int(input("Passo: "))
if c == 0:
    c = 1

contador(a, b, c)
