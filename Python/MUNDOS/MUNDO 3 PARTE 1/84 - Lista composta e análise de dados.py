lista = []
pesos = []
pesadas = []
leves = []

while True:
    nome = str(input("Digite seu nome: "))
    peso = float(input("Digite seu peso, em Kg: "))
    lista.append([nome, peso])
    pesos.append(peso)

    escolha = int(input('''Deseja adicionar mais pessoas?
    [0] - Não
    [1] - Sim'''))
    if escolha == 0:
        break

for pessoas in lista:
    if pessoas[1] >= max(pesos):
        pesadas.append(pessoas[0])
    if pessoas[1] <= min(pesos):
        leves.append((pessoas[0]))

print(f"Foram cadastradas {len(lista)} pessoas na lista")
print(f"As pessoas mais pesadas foram: {pesadas}")
print(f"As pessoas mais leves foram: {leves}")
