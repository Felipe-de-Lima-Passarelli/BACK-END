while True:
    H1, M1, H2, M2 = map(int, input().split())
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break

    tempo = 0

    if H1 == H2 and M1 == M2:
        tempo = 1440
    elif H1 <= H2 and M1 <= M2:
        tempo = ((H2 - H1) * 60) + (M2 - M1)
    elif H1 == H2 and M1 >= M2:
        tempo = (24 * 60) - (M1 - M2)
    elif H1 < H2 and M1 > M2:
        tempo = ((H2 - H1) * 60) - (M1 - M2)
    else:
        if M2 >= M1:
            tempo = ((24 - H1) * 60) + (H2 * 60) + (M2 - M1)
        else:
            tempo = ((24 - H1) * 60) + (H2 * 60) - (M1 - M2)

    print(tempo)
