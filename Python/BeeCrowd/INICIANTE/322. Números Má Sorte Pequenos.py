N = int(input())
N = str(N)
azar = False

for i in range(0, len(N)):
    if i != (len(N) - 1):
        if N[i] == "1":
            if N[i + 1] == "3":
                azar = True
                break

if azar:
    print(f"{N} es de Mala Suerte")
else:
    print(f"{N} NO es de Mala Suerte")
