contagemdentro = 0
contagemfora = 0

N = int(input())
while N > 10000:
    N = int(input())

listaX = []

for i in range(0, N):
    X = int(input())
    listaX.append(X)

for i in listaX:
    if i >= 10 and i <= 20:
        contagemdentro += 1
    else:
        contagemfora += 1
print(f"{contagemdentro} in")
print(f"{contagemfora} out")
