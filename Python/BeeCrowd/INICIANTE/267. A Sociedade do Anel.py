N = int(input())
A, E, H, M, X = 0, 0, 0, 0, 0

for _ in range(0, N):
    nome, raca = map(str, input().split())
    if raca == "A":
        A += 1
    elif raca == "E":
        E += 1
    elif raca == "H":
        H += 1
    elif raca == "M":
        M += 1
    else:
        X += 1

print(f"{X} Hobbit(s)")
print(f"{H} Humano(s)")
print(f"{E} Elfo(s)")
print(f"{A} Anao(oes)")
print(f"{M} Mago(s)")
