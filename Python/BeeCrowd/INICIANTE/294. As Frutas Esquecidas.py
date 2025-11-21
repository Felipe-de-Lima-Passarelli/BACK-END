N, M = map(int, input().split())
frutas = []
testes = []

for _ in range(0, N):
    frutas.append(input().lower())

for _ in range(0, M):
    x = input().lower()
    testes.append(x)
    x = x[::-1]
    testes.append(x)

for fruta in frutas:
    contador = 0
    for palavras in testes:
        if fruta in palavras:
            contador += 1
    if contador > 0:
        print(f"Sheldon come a fruta {fruta}")
    else:
        print(f"Sheldon detesta a fruta {fruta}")
