A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

areatriangulo = (A*C)/2
areacirculo = pi*(C**2)
areatrapezio = ((A+B)*C)/2
areaquadrado = B*B
arearetangulo = A*B

print(f"TRIANGULO: {areatriangulo:.3f}")
print(f"CIRCULO: {areacirculo:.3f}")
print(f"TRAPEZIO: {areatrapezio:.3f}")
print(f"QUADRADO: {areaquadrado:.3f}")
print(f"RETANGULO: {arearetangulo:.3f}")
