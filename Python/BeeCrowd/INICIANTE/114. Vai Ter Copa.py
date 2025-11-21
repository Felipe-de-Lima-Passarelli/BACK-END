while True:
    try:
        N = int(input())
    except EOFError:
        break

    while N < 0 or N > 100:
        N = int(input())

    if N == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")
