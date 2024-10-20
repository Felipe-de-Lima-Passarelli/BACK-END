from random import randint

numeros = []

def sorteia():
    print("Sorteando 5 valores da lista: ", end = "")
    for i in range(0, 5):
        x = randint(1, 10)
        print(x, end = " -> ")
        numeros.append(x)
    print("PRONTO!")

def somapar():
    somapares = 0
    for valores in numeros:
        if valores%2 == 0:
            somapares += valores
    print(f"Somando os valores pares de {numeros}, temos {somapares}")

sorteia()
somapar()
