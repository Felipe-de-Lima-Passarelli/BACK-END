n = int(input())
x = n**2
brancas = 0

for i in range(0, n):
    if n%2 != 0:
        if i%2 == 0:
            brancas += int(n/2) + 1
        else:
            brancas += int(n/2)
    else:
        brancas = int(x/2)

print(f"{brancas} casas brancas e {x - brancas} casas pretas")
