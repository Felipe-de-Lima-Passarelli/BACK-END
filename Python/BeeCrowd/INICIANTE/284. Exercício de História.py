while True:
    try:
        N = int(input())
        seculo = 1
        while N > 10000000:
            seculo += 100000
            N -= 10000000
        while N > 1000000:
            seculo += 10000
            N -= 1000000
        while N > 100000:
            seculo += 1000
            N -= 100000
        while N > 10000:
            seculo += 100
            N -= 10000
        while N > 1000:
            seculo += 10
            N -= 1000
        while N > 100:
            seculo += 1
            N -= 100

        print(seculo)

    except EOFError:
        break
