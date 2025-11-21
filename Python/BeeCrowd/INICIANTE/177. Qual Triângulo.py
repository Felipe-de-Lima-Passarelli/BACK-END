A, B, C = map(int, input().split())
medidas = [A, B, C]
medidas.sort()
hipotenusa = medidas[2]
cateto1 = medidas[0]
cateto2 = medidas[1]
retangulo = False

if hipotenusa**2 == (cateto1**2) + (cateto2**2):
    retangulo = True

if (A + B) > C and (A + C) > B and (B + C) > A:
    if A == B == C:
        if retangulo:
            print(f"Valido-Equilatero")
            print(f"Retangulo: S")
        else:
            print(f"Valido-Equilatero")
            print(f"Retangulo: N")
    elif A == B or A == C or B == C:
        if retangulo:
            print(f"Valido-Isoceles")
            print(f"Retangulo: S")
        else:
            print(f"Valido-Isoceles")
            print(f"Retangulo: N")
    else:
        if retangulo:
            print(f"Valido-Escaleno")
            print(f"Retangulo: S")
        else:
            print(f"Valido-Escaleno")
            print(f"Retangulo: N")
else:
    print(f"Invalido")
