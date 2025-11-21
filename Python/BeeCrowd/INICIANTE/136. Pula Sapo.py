P, N = map(int, input().split())
while P < 1 or P > 5 or N < 2 or N > 100:
    P, N = map(int, input().split())

win = True
dados = []
entrada = map(int, input().split())

for num in entrada:
    dados.append(num)

while len(dados) != N:
    dados = []
    entrada = map(int, input().split())

    for num in entrada:
        dados.append(num)

c = 0
for i in range(0, (N - 1)):
    x = abs(dados[1 + c] - dados[c])
    if x > P:
        win = False
    c += 1

if not win:
    print("GAME OVER")
else:
    print("YOU WIN")
