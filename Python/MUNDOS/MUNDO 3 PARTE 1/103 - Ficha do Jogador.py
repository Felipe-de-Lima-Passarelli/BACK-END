def ficha(nome = "<desconhecido>", gols = "0"):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

name = str(input("Nome do Jogador: "))
golsmarcados = (input("Número de Gols: "))

if name == "" and golsmarcados != "":
    ficha(gols = golsmarcados)
elif golsmarcados == "" and name != "":
    ficha(nome = name)
elif name == "" and golsmarcados == "":
    ficha()
else:
    ficha(name, golsmarcados)
