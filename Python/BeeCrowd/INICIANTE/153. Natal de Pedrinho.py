while True:
    try:
        tempo = 0
        mes, dia = map(int, input().split())
    except EOFError:
        break

    match mes:
        case 1:
            tempo = 360 - dia
        case 2:
            tempo = 329 - dia
        case 3:
            tempo = 300 - dia
        case 4:
            tempo = 269 - dia
        case 5:
            tempo = 239 - dia
        case 6:
            tempo = 208 - dia
        case 7:
            tempo = 178 - dia
        case 8:
            tempo = 147 - dia
        case 9:
            tempo = 116 - dia
        case 10:
            tempo = 86 - dia
        case 11:
            tempo = 55 - dia
        case 12:
            tempo = 25 - dia

    if tempo == 0:
        print("E natal!")
    elif tempo == 1:
        print("E vespera de natal!")
    elif tempo > 0:
        print(f"Faltam {tempo} dias para o natal!")
    else:
        print("Ja passou!")
