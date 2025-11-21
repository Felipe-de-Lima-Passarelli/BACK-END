A = float(input())
while A < 0 or A > 10:
    A = float(input())

B = float(input())
while B < 0 or B > 10:
    B = float(input())

media = ((A * 3.5) + (B * 7.5)) / 11
print(f"MEDIA = {media:.5f}")
