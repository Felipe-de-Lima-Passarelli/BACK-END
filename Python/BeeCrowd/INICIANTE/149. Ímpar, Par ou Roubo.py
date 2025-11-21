p, j1, j2, r, a = map(int, input().split())
while p < 0 or p > 1 or r < 0 or r > 1 or a < 0 or a > 1 or j1 < 1 or j1 > 100 or j2 < 1 or j2 > 100:
    p, j1, j2, r, a = map(int, input().split())

if p == 1:
    if (j1+j2)%2 == 0:
        if a == 0:
            print("Jogador 1 ganha!")
        else:
            if r == 1:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
    else:
        if r == 1:
            if a == 0:
                print("Jogador 1 ganha!")
            else:
                print("Jogador 2 ganha!")
        else:
            if a == 0:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
else:
    if (j1+j2)%2 != 0:
        if a == 0:
            print("Jogador 1 ganha!")
        else:
            if r == 1:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
    else:
        if r == 1:
            if a == 0:
                print("Jogador 1 ganha!")
            else:
                print("Jogador 2 ganha!")
        else:
            if a == 0:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
