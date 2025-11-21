x1 = 234.345
x2 = 45.698
c1 = x1
c2 = x2
contador1 = 0
contador2 = 0

while c1 >= 10:
    contador1 += 1
    c1 /= 10
while c2 >= 10:
    contador2 += 1
    c2 /= 10

print(f"{x1:.6f} - {x2:.6f}")
print(f"{x1:.0f} - {x2:.0f}")
print(f"{x1:.1f} - {x2:.1f}")
print(f"{x1:.2f} - {x2:.2f}")
print(f"{x1:.3f} - {x2:.3f}")
print(f"{c1:.6f}e+{contador1:02} - {c2:.6f}e+{contador2:02}")
print(f"{c1:.6f}E+{contador1:02} - {c2:.6f}E+{contador2:02}")
print(f"{x1} - {x2}")
print(f"{x1} - {x2}")
