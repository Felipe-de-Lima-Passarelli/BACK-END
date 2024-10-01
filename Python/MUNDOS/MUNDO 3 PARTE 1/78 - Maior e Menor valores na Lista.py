lista = [float(input("Digite o 1º número")),
         float(input("Digite o 2º número")),
         float(input("Digite o 3º número")),
         float(input("Digite o 4º número")),
         float(input("Digite o 5º número"))]

maior = []
menor = []

for i, n in enumerate(lista):
    if n == max(lista):
        maior.append(i + 1)
    if n == min(lista):
        menor.append(i + 1)


print(f"O maior valor encontrado na lista foi: {max(lista)}")
print(f"O menor valor encontrado na lista foi: {min(lista)}")
print(f"O valor máximo está nas posições: {maior}, enquanto o valor mínimo apareceu nas posições: {menor}.")
