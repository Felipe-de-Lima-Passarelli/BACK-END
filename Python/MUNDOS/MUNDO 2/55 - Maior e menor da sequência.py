menor = 999999999999
maior = 0

for i in range(0,5):
    peso = float(input("Digite seu peso, em Kg: "))
    if peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso

print("O maior peso, em Kg, foi {}".format(maior))
print("O menor peso, em Kg, foi {}".format(menor))
