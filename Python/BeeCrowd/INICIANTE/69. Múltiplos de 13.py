X = int(input())
Y = int(input())

listanum = []
soma = 0

if X > Y:
    for i in range(Y, X+1):
        listanum.append(i)
else:
    for i in range(X, Y+1):
        listanum.append(i)

for num in listanum:
    if num%13 != 0:
        soma += num

print(soma)
