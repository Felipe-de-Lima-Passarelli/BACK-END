while True:
    try:
        H = str(input()).split(":")
        while int(H[0]) < 5 or int(H[0]) > 9 or int(H[1]) < 0 or int(H[1]) > 59:
            H = str(input()).split(":")
    except EOFError:
        break

    if int(H[0]) < 7:
        print("Atraso maximo: 0")
    elif int(H[0]) == 7:
        if int(H[1]) == 0:
            print("Atraso maximo: 0")
        else:
            print(f"Atraso maximo: {int(H[1])}")
    else:
        print(f"Atraso maximo: {((int(H[0]) - 7) * 60) + int(H[1])}")
