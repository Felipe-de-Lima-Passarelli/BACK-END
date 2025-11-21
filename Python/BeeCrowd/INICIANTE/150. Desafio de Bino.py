N = int(input())
while N < 1 or N > 1000:
    N = int(input())

dados = list(map(int, input().split()))
while len(dados) != N:
    dados = list(map(int, input().split()))

multiplo2, multiplo3, multiplo4, multiplo5 = 0, 0, 0, 0

for num in dados:
    if num%2 == 0:
        multiplo2 += 1
    if num%3 == 0:
        multiplo3 += 1
    if num%4 == 0:
        multiplo4 += 1
    if num%5 == 0:
        multiplo5 += 1

print(f"{multiplo2} Multiplo(s) de 2")
print(f"{multiplo3} Multiplo(s) de 3")
print(f"{multiplo4} Multiplo(s) de 4")
print(f"{multiplo5} Multiplo(s) de 5")
