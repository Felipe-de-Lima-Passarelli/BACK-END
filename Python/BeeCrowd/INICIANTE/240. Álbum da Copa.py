N = int(input())
M = int(input())
cartastotal = []

for _ in range(0, M):
    carta = int(input())
    if carta not in cartastotal:
        cartastotal.append(carta)

print(f"{N - len(cartastotal)}")
