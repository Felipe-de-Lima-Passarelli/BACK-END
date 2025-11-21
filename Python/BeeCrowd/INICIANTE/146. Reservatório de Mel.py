n = 3.14

while True:
    try:
        V = float(input())
        while V < 1 or V > 10000:
            V = float(input())

        D = float(input())
        while D < 1 or D > 100:
            D = float(input())
    except EOFError:
        break

    area = n *((D/2)**2)
    altura = V/area

    print(f"ALTURA = {altura:.2f}")
    print(f"AREA = {area:.2f}")
