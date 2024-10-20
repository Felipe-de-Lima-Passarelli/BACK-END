from time import sleep

jogador = dict()
gols = []
total = 0

jogador["Nome"] = str(input("Digite o nome do Jogador"))
partidas = int(input(f"Quantas partidas {jogador["Nome"]} jogou?"))

for i in range(1, (partidas + 1)):
    gols.append(int(input(f"Quantos gols na partida {i}?")))
    total += gols[i - 1]

jogador["gols"] = gols
jogador["Total"] = total

print(50*"-=")
print(jogador)
print(50*"-=")
print(f"O campo {list(jogador.keys())[0]} tem o valor {jogador["Nome"]}")
print(f"O campo {list(jogador.keys())[1]} tem o valor {jogador["gols"]}")
print(f"O campo {list(jogador.keys())[2]} tem o valor {jogador["Total"]}")
print(50*"-=")
print(f"O jogador {jogador["Nome"]} jogou {partidas}.")
for i in range(1, (partidas + 1)):
    print(f"Na partida {i}, fez {list(jogador.values())[1][i - 1]} gols")
    sleep(1)
print(f"Foi um total de {jogador["Total"]} gols")
