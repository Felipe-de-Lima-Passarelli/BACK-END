p = int(input())
while p < 1 or p > 5:
    p = int(input())

preco = 0

for i in range(0, p):
    codigo, q = map(int, input().split())
    while q < 1 or q > 500:
        codigo, q = map(int, input().split())
    if codigo == 1001:
        preco += 1.50 * q
    elif codigo == 1002:
        preco += 2.50 * q
    elif codigo == 1003:
        preco += 3.50 * q
    elif codigo == 1004:
        preco += 4.50 * q
    else:
        preco += 5.50 * q

print(f"{preco:.2f}")
