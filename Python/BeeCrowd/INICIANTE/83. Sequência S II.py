soma = 0
a = 1
b = 1

for i in range(1, 21):
    if i == 1:
        soma += a
        a+= 2
    else:
        soma += a/(2**b)
        a += 2
        b += 1

print(f"{soma:.2f}")
