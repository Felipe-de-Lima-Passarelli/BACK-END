N, G = map(int, input().split())
runas = []
valores = []
contador = 0

for _ in range(0, N):
    R, V = input().split()
    R = str(R)
    V = int(V)
    runas.append(R)
    valores.append(V)

X = int(input())
runasutilizadas = list(map(str, input().split()))

for cadaruna in runasutilizadas:
    posicao = runas.index(cadaruna)
    contador += valores[posicao]

print(contador)

if contador < G:
    print("My precioooous")
else:
    print("You shall pass!")
