M, N = input().split()
M = int(M)
N = int(N)

while True:
    lista = []
    if M <= 0 or N <= 0:
        break
    else:
        if N > M:
            N, M = M, N
        while N <= M:
            lista.append(N)
            N += 1
        for i in lista:
            print(i, end = " ")
        print(f"Sum={sum(lista)}")
        M, N = input().split()
        M = int(M)
        N = int(N)
