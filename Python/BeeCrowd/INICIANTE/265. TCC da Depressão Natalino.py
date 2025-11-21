E, D = map(int, input().split())

if E < D:
    if D <= 21:
        print("Muito bem! Apresenta antes do Natal!")
    elif D <= 24:
        if D + 2 <= 24:
            print("Parece o trabalho do meu filho!")
            print("TCC Apresentado!")
        else:
            print("Parece o trabalho do meu filho!")
            print("Fail! Entao eh nataaaaal!")
else:
    print("Eu odeio a professora!")
