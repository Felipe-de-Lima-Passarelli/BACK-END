while True:
    try:
        X, Y, M = map(int, input().split())
        for _ in range(0, M):
            Xi, Yi = map(int, input().split())
            if (Xi <= X and Yi <= Y) or (Xi <= Y and Yi <= X):
                print("Sim")
            else:
                print("Não")
    except EOFError:
        break
