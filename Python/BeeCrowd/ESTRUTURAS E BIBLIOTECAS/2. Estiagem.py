cidade = 1

while True:
    N = int(input())
    if N == 0:
        break

    agrupamento = {}

    total_pessoas = 0
    total_consumo = 0

    for _ in range(N):
        X, Y = map(int, input().split())
        consumo_arredondado = Y // X

        if consumo_arredondado not in agrupamento:
            agrupamento[consumo_arredondado] = 0
        agrupamento[consumo_arredondado] += X

        total_pessoas += X
        total_consumo += Y

    agrupamento_ordenado = sorted(agrupamento.items())

    print(f"Cidade# {cidade}:")
    for consumo, pessoas in agrupamento_ordenado:
        print(f"{pessoas}-{consumo}", end=" ")
    print()

    consumo_medio = total_consumo / total_pessoas
    consumo_medio_str = f"{consumo_medio:.10f}"
    consumo_medio_cortado = consumo_medio_str[:consumo_medio_str.index('.') + 3]
    print(f"Consumo medio: {consumo_medio_cortado} m3.\n")

    cidade += 1
