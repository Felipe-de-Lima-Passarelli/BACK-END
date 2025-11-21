while True:
    K, L = map(int, input().split())
    if K == 0 and L == 0:
        break

    L -= 1
    numero = 0
    contador = 0

    for i in range(2, L):
        if K%i == 0:
            contador += 1
            numero = i
            break

    if contador == 0:
        print("GOOD")
    else:
        print(f"BAD {numero}")
