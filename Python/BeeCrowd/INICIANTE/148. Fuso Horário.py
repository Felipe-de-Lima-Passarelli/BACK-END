S, T, F = map(int, input().split())
while S < 0 or S > 23 or T < 1 or T > 12 or F < -5 or F > 5:
    S, T, F = map(int, input().split())

horachegada = S + T + F

if horachegada > 24:
    horachegada -= 24
elif horachegada == 24:
    horachegada = 0
elif horachegada < 0:
    horachegada += 24

print(horachegada)
