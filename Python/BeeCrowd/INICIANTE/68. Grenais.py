totalpartidas = 0
inter = 0
gremio = 0
empate = 0

while True:
    X, Y = input().split()
    X = int(X)
    Y = int(Y)

    totalpartidas += 1
    if X > Y:
        inter += 1
    elif X < Y:
        gremio += 1
    else:
        empate += 1

    escolha = int(input("Novo grenal (1-sim 2-nao)\n"))
    if escolha == 2:
        break

print(f"{totalpartidas} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")
if inter > gremio:
    print(f"Inter venceu mais")
elif gremio > inter:
    print(f"Gremio venceu mais")
