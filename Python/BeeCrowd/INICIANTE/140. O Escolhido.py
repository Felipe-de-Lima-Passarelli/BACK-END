n = int(input())
melhoraluno = []
while n < 3 or n > 100:
    n = int(input())

for i in range(0, n):
    m, nota = input().split()
    m = int(m)
    nota = float(nota)
    while m <= 0 or m > 1000000 or nota < 0 or nota > 10:
        m, nota = input().split()
        m = int(m)
        nota = float(nota)
    if i == 0:
        melhoraluno.append(m)
        melhoraluno.append(nota)

    if nota > melhoraluno[1]:
        melhoraluno[0] = m
        melhoraluno[1] = nota

if melhoraluno[1] >= 8:
    print(f"{melhoraluno[0]}")
else:
    print("Minimum note not reached")
