from time import sleep
from random import sample
lista = []
palpites = int(input("Digite quantos palpites deseja fazer na mega-sena: "))
while palpites <= 0:
    print("Digite um número válido")
    sleep(1)
    palpites = int(input("Digite quantos palpites deseja fazer na mega-sena: "))

for i in range(0, palpites):
    random = sample(range(1, 61), 6)
    lista.append(random)
    lista[i].sort()

for i in lista:
    print(i)
    sleep(1)
