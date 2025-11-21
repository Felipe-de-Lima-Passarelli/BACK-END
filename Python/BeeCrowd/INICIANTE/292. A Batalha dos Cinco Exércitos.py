H, E, A, O, W, X = map(int, input().split())

soma_bem = H + E + A + X
soma_mal = O + W

if soma_bem >= soma_mal:
    print("Middle-earth is safe.")
else:
    print("Sauron has returned.")
