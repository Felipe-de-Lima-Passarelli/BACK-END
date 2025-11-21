N = int(input())
ruas = []

for _ in range(0, N):
   dados = list(map(int, input().split()))
   nome = dados[0]
   conexoes = dados[1]
   ruas_conectadas = dados[2:]
   ruas.append([nome, conexoes, ruas_conectadas])

problemas = 0
sem_estrada = True

for estradas in ruas:
    if estradas[1] == 0:
        print(f"TRAPPED {estradas[0]}")
        problemas += 1

if problemas == 0:
    print("NO PROBLEMS")
