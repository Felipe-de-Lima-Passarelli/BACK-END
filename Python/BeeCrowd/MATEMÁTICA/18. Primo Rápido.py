def primo(x):
    if x < 2:
        print("Not Prime")
        return
    if x == 2:
        print("Prime")
        return
    if x % 2 == 0:
        print("Not Prime")
        return
    for i in range(3, int(x**(1/2)) + 1, 2):
        if x % i == 0:
            print("Not Prime")
            return
    print("Prime")

N = int(input())

for _ in range(N):
    valor = int(input())
    primo(valor)
