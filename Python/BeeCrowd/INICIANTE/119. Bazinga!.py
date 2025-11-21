T = int(input())
while T <= 0 or T > 100:
    T = int(input())

for i in range(1, (T + 1)):
    dados = input().split()
    while len(dados) != 2:
        dados = input().split()

    sheldon, raj = dados

    if sheldon == "pedra":
        if raj == "lagarto" or raj == "tesoura":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "pedra":
            print(f"Caso #{i}: De novo!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    elif sheldon == "papel":
        if raj == "pedra" or raj == "Spock":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "papel":
            print(f"Caso #{i}: De novo!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    elif sheldon == "tesoura":
        if raj == "papel" or raj == "lagarto":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "tesoura":
            print(f"Caso #{i}: De novo!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    elif sheldon == "lagarto":
        if raj == "Spock" or raj == "papel":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "lagarto":
            print(f"Caso #{i}: De novo!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    else:
        if raj == "tesoura" or raj == "pedra":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "Spock":
            print(f"Caso #{i}: De novo!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")
