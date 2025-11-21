A = round(float(input()), 1)
while A < 0 or A > 10:
    A = round(float(input()), 1)

B = round(float(input()), 1)
while B < 0 or B > 10:
    B = round(float(input()), 1)

C = round(float(input()), 1)
while C < 0 or C > 10:
    C = round(float(input()), 1)

media = ((A*2) + (B*3) + (C*5))/10
print(f"MEDIA = {media:.1f}")
