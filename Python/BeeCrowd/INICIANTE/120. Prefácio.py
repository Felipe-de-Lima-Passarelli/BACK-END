a, b = input().split()
a = int(a)
b = int(b)

while a < -1000 or b > 1000 or b == 0:
    a, b = input().split()
    a = int(a)
    b = int(b)

r = a%abs(b)
q = int(((a - r)/b))

print(f"{q}", end = " ")
print(r)
