from time import sleep
lista = []

for c in range(0, 5):
    x = int(input("Digite um número inteiro positivo: "))
    while x <= 0:
        print("Número Inválido")
        sleep(1)
        x = int(input("Digite um número inteiro positivo: "))
    if x in lista:
        print("Número já cadastrado, tente outro")
        sleep(1)
        x = int(input("Digite um número inteiro positivo: "))
        while x <= 0 or x in lista:
            print("Número já cadastrado ou inválido, tente outro")
            sleep(1)
            x = int(input("Digite um número inteiro positivo: "))
        if not lista or x > lista[-1]:
            lista.append(x)
        else:
            for i in range(len(lista)):
                if x < lista[i]:
                    lista.insert(i, x)
                    break
    else:
        if not lista or x > lista[-1]:
            lista.append(x)
        else:
            for i in range(len(lista)):
                if x < lista[i]:
                    lista.insert(i, x)
                    break
print(lista)
