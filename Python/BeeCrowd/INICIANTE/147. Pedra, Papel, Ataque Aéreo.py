N = int(input())
while N < 1 or N > 1000:
    N = int(input())

for i in range(0, N):
    escolha1 = str(input())
    while escolha1 != "ataque" and escolha1 != "pedra" and escolha1 != "papel":
        escolha1 = str(input())

    escolha2 = str(input())
    while escolha2 != "ataque" and escolha2 != "pedra" and escolha2 != "papel":
        escolha2 = str(input())

    if escolha1 == "ataque":
        if escolha2 == "pedra":
            print("Jogador 1 venceu")
        elif escolha2 == "papel":
            print("Jogador 1 venceu")
        else:
            print("Aniquilacao mutua")

    if escolha1 == "pedra":
        if escolha2 == "papel":
            print("Jogador 1 venceu")
        elif escolha2 == "ataque":
            print("Jogador 2 venceu")
        else:
            print("Sem ganhador")

    if escolha1 == "papel":
        if escolha2 == "papel":
            print("Ambos venceram")
        elif escolha2 == "pedra":
            print("Jogador 2 venceu")
        else:
            print("Jogador 2 venceu")
