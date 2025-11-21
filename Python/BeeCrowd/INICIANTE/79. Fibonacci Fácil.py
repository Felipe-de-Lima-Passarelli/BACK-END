N = int(input())
primeironum = 0
segundonum = 1
terceironum = 1

while N >= 46:
    N = int(input())

for i in range(0, N):
    if i == 0:
        print(0, end=" ")
    elif i == 1:
        print(1, end=" ")
    elif i == N - 1:
        print(f"{terceironum}")
    else:
        print(f"{terceironum}", end = " ")
        primeironum = segundonum
        segundonum = terceironum
        terceironum = primeironum + segundonum
