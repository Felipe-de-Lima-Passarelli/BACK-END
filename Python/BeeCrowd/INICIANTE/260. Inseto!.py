while True:
    try:
        C = int(input())
        for _ in range(0, C):
            N = int(input())
            if N <= 8000:
                print("Inseto!")
            else:
                print("Mais de 8000!")
    except EOFError:
        break
