T = int(input())

contador = 1

for _ in range(0, T):
    conversao = str(input())
    R, G, B = map(int, input().split())
    valores = [R, G, B]

    if conversao == "eye":
        resposta = int(0.3*R + 0.59*G + 0.11*B)
        print(f"Caso #{contador}: {resposta}")
        contador += 1
    elif conversao == "mean":
        resposta = int((R+G+B)/3)
        print(f"Caso #{contador}: {resposta}")
        contador += 1
    elif conversao == "max":
        resposta = max(valores)
        print(f"Caso #{contador}: {resposta}")
        contador += 1
    else:
        resposta = min(valores)
        print(f"Caso #{contador}: {resposta}")
        contador += 1
