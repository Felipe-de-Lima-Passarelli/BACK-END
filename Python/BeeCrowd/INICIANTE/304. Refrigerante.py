E, F, C = map(int, input().split())
soma = E + F
total = 0

while soma >= C:
    total += 1
    soma -= C - 1

print(total)
