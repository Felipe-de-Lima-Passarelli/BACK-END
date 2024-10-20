from time import sleep

lista = [[], []]
for c in range(0, 6):
    x = int(input("Digite um valor inteiro positivo: "))
    while x <= 0:
        print("Número inválido")
        sleep(1)
        x = int(input("Digite um valor inteiro positivo: "))
    if x%2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)

lista[0].sort()
lista[1].sort()
print(f"Os valores pares digitados foram: {lista[0]}")
print(f"Os valores ímpares digitados foram: {lista[1]}")
