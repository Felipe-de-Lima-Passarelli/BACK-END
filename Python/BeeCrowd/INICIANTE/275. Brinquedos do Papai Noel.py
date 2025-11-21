N = int(input())
carrinho = 0
boneca = 0

for _ in range(0, N):
    nome, sexo = map(str, input().split())
    if sexo == "M":
        carrinho += 1
    else:
        boneca += 1

print(f"{carrinho} carrinhos")
print(f"{boneca} bonecas")
