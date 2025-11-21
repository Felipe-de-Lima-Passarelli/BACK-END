k, n = map(int, input().split())
y, p = map(int, input().split())
karl = [y, p]
participantes = []

for i in range(0, (n + k - 2)):
    y, p = map(int, input().split())
    participantes.append([y, p])

ano_inicio = 2011
ano_final = karl[0]

personagem = []
resultado_para_retirar = []
chave_final = [karl]
forca = 0

while ano_inicio != ano_final:
    for i in range(0, len(participantes)):
        if participantes[i][0] == ano_inicio and participantes[i][1] > forca:
            forca = participantes[i][1]
            personagem = participantes[i]
    ano_inicio += 1
    resultado_para_retirar.append(personagem)


for palavras in participantes:
    if palavras not in resultado_para_retirar:
        chave_final.append(palavras)

chave_resposta = []
campeao = ""

for palavras in chave_final:
    if palavras[0] > ano_final:
        pass
    else:
        chave_resposta.append(palavras)

for respostas in chave_resposta:
    if respostas == chave_resposta[0]:
        campeao = respostas
    else:
        if respostas[1] > campeao[1]:
            campeao = respostas

if campeao == chave_resposta[0]:
    print(campeao[0])
else:
    print("unknown")
