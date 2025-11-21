V = int(input())
while V < 1 or V > 2000000000:
    V = int(input())

print(hex(V)[2:].upper())
