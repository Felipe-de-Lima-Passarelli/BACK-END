N = int(input())
while N <= 1 or N > 100:
    N = int(input())

dados = list(map(int, input().split()))
for i in range(0, (N - 1)):
    if dados[i] > dados[i + 1]:
        resultado = i + 2
        break

try:
    print(resultado)
except NameError:
    print(0)
