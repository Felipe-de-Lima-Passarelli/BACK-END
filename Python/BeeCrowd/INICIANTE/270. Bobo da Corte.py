N = int(input())
votos = []
for _ in range(0, N):
    votos.append(int(input()))

if votos[0] == max(votos):
    print("S")
else:
    print("N")
