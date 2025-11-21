n = int(input())
habilidades = []

for _ in range(0, n):
    habilidades.append(input())

vitorias = 0

for skills in habilidades:
    posicao = 0
    derrota = 0
    for letras in skills:
        if posicao != (len(skills) - 1):
            if skills[posicao] == "C":
                if skills[posicao + 1] == "D":
                    derrota += 1
        posicao += 1
    if derrota == 0:
        vitorias += 1

print(vitorias)
