while True:
    try:
        a, b, c = map(int, input().split())

        area_total = 3.1415926535897*((c/2)**2)
        metade_perimetro = (a + b + c ) / 2
        area_triangulo = (metade_perimetro * (metade_perimetro - a) * (metade_perimetro - b) * (metade_perimetro - c)) ** (1/2)
        area_circulo = 3.1415926535897*((area_triangulo/metade_perimetro)**2)

        print(f"{area_total - area_triangulo:.4f} {area_triangulo - area_circulo:.4f} {area_circulo:.4f}")

    except EOFError:
        break
