n = int(input())
while n <= 0 or n > 50:
    n = int(input())

resultado = (((1 + (5**(1/2)))/2)**n - ((1 - (5**(1/2)))/2)**n)/(5**(1/2))
print(f"{resultado:.1f}")
