while True:
    try:
        papel = 0
        pedra = 0
        tesoura = 0
        dodo, leo, pepper = map(str, input().split())

        if dodo == "papel":
            papel += 1
        elif dodo == "pedra":
            pedra += 1
        else:
            tesoura += 1

        if leo == "papel":
            papel += 1
        elif leo == "pedra":
            pedra += 1
        else:
            tesoura += 1

        if pepper == "papel":
            papel += 1
        elif pepper == "pedra":
            pedra += 1
        else:
            tesoura += 1

        if papel == 3 or pedra == 3 or tesoura == 3:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        elif papel == 1 and pedra == 1 and tesoura == 1:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        elif papel == 2 and pedra == 1:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        elif papel == 2 and tesoura == 1:
            if dodo == "tesoura":
                print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
            elif leo == "tesoura":
                print("Iron Maiden's gonna get you, no matter how far!")
            else:
                print("Urano perdeu algo muito precioso...")
        elif pedra == 2 and papel == 1:
            if dodo == "papel":
                print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
            elif leo == "papel":
                print("Iron Maiden's gonna get you, no matter how far!")
            else:
                print("Urano perdeu algo muito precioso...")
        elif pedra == 2 and tesoura == 1:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        elif tesoura == 2 and pedra == 1:
            if dodo == "pedra":
                print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
            elif leo == "pedra":
                print("Iron Maiden's gonna get you, no matter how far!")
            else:
                print("Urano perdeu algo muito precioso...")
        elif tesoura == 2 and papel == 1:
            print("Putz vei, o Leo ta demorando muito pra jogar...")

    except EOFError:
        break
