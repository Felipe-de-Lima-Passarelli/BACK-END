A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

delta = B**2 - (4*A*C)
if delta < 0:
    print("Impossivel calcular")
else:
    try:
        x1 = (-B + (delta**(1/2)))/(2*A)
        x2 = (-B - (delta**(1/2)))/(2*A)
    except ZeroDivisionError:
        print("Impossivel calcular")
    else:
        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")
