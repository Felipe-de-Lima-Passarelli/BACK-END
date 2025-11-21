while True:
    try:
        M = float(input())

        if M < 90 or M == 360:
            print("Bom Dia!!")
            if M == 360:
                horas, minutos, segundos = 6, 0, 0
            else:
                horas, minutos, segundos = 6, 0, M * 240
        elif M < 180:
            print("Boa Tarde!!")
            M -= 90
            horas, minutos, segundos = 12, 0, M * 240
        elif M < 270:
            print("Boa Noite!!")
            M -= 180
            horas, minutos, segundos = 18, 0, M * 240
        else:
            print("De Madrugada!!")
            M -= 270
            horas, minutos, segundos = 0, 0, M * 240

        minutos += int(segundos // 60)
        segundos %= 60
        horas += minutos // 60
        minutos %= 60

        print(f"{horas:02}:{minutos:02}:{int(segundos):02}")
    except EOFError:
        break
