T = int(input())
while T < 1 or T > 4:
    T = int(input())

A, B, C, D, E = map(int, input().split())
while A < 1 or A > 4 or B < 1 or B > 4 or C < 1 or C > 4 or D < 1 or D > 4 or E < 1 or E > 4:
    A, B, C, D, E = map(int, input().split())

contagem = 0
dados = [A, B, C, D, E]
for num in dados:
    if num == T:
        contagem += 1

print(contagem)
