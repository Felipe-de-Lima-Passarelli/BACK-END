N = int(input())
while N < 1 or N > 100000:
    N = int(input())

anoatual = 2015

for i in range(0, N):
    x = int(input())
    resultado = abs(anoatual - x)
    if x >= anoatual:
        print(f"{resultado + 1} A.C.")
    else:
        print(f"{resultado} D.C.")
