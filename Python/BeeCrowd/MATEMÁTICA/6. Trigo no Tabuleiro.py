N = int(input())

for _ in range(0, N):
    X = int(input())
    peso_total_em_gramas = 0
    for casas in range(0, X):
        peso_total_em_gramas += 2 ** casas
    print(f"{int((peso_total_em_gramas/12)/1000)} kg")
