N = int(input())
posicao_inicial_moeda = str(input())

for _ in range(0, N):
    movimento = int(input())
    if movimento == 1:
        if posicao_inicial_moeda != "C":
            if posicao_inicial_moeda == "A":
                posicao_inicial_moeda = "B"
            else:
                posicao_inicial_moeda = "A"
    elif movimento == 2:
        if posicao_inicial_moeda != "A":
            if posicao_inicial_moeda == "B":
                posicao_inicial_moeda = "C"
            else:
                posicao_inicial_moeda = "B"
    else:
        if posicao_inicial_moeda != "B":
            if posicao_inicial_moeda == "A":
                posicao_inicial_moeda = "C"
            else:
                posicao_inicial_moeda = "A"

print(posicao_inicial_moeda)
