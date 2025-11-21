x = float(input())

if x > 100 or x < 0:
    print("Fora de intervalo")
elif x > 75:
    print(f"Intervalo (75,100]")
elif x > 50:
    print(f"Intervalo (50,75]")
elif x > 25:
    print(f"Intervalo (25,50]")
else:
    print(f"Intervalo [0,25]")
