while True:
    try:
        h, m = map(int, input().split())

        horas = int(h/30)
        if horas == 12:
            horas = 0

        minutos = int(m/6)
        if minutos == 60:
            minutos = 0

        print(f"{horas:02}:{minutos:02}")

    except EOFError:
        break
