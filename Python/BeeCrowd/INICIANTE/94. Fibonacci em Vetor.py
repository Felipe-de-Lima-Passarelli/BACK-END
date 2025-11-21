T = int(input())

for i in range(0, T):
    lista = [0, 1]
    primeironum = 0
    segundonum = 1
    N = int(input())
    while N < 0 or N > 60:
        N = int(input())

    while len(lista) <= N:
        terceironum = primeironum + segundonum
        lista.append(terceironum)
        primeironum, segundonum = segundonum, terceironum

    print(f"Fib({N}) = {lista[N]}")
