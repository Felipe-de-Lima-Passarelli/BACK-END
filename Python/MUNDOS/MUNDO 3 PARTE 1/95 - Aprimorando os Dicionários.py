from time import sleep
from copy import deepcopy

Jogador = dict()
todosJogadores = dict()
listaGol = []
c = 0

while True:
    i = 0
    total = 0
    Jogador["Nome"] = str(input("Digite o nome do jogador: "))
    partidas = int(input(f"Quantas partidas {Jogador["Nome"]} jogou? : "))
    for i in range(partidas):
        gols = int(input(f"Quantos gols fez na partida {i + 1}? : "))
        listaGol.append(gols)
        total += gols
        i += 1

    Jogador["Gol"] = listaGol
    Jogador["Total"] = total
    todosJogadores[c] = deepcopy(Jogador)
    c += 1
    Jogador.clear()
    listaGol.clear()
    escolha = int(input('''Deseja cadastrar outro jogador?
    [0] - Não
    [1] - Sim'''))
    if escolha == 0:
        break

print(50*"-=")
print("{Cód}  Nome      Gols        Total")

for i in todosJogadores.items():
    print(f"{i[0]}     {i[1]["Nome"]}    {i[1]["Gol"]}        {i[1]["Total"]}")

continuar = str(input("Deseja analisar algum jogador? [S/N]"))
if continuar.strip() in "Nn":
    print("Fim do Programa")
else:
    for i in todosJogadores.items():
        print(f"{i[0]}     {i[1]["Nome"]}")
    escolhaJogador = int(input("Qual jogador deseja analisar?"))
    print(f"{list(todosJogadores.items())[escolhaJogador][1]}")
