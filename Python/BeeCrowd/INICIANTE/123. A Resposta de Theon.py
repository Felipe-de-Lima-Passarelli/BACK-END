N = int(input())
while N < 1 or N > 100:
    N = int(input())

opcoes = []
dados = input().split()
dados = list(map(int, dados))

while len(dados) != N:
    dados = input().split()
    dados = list(map(int, dados))

menor = ""
for posicao, num in enumerate(dados):
    if posicao == 0:
        menor = num
    else:
        if num < menor:
            menor = num

print(dados.index(menor) + 1)
