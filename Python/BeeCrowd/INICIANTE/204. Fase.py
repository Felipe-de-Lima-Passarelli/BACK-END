N = int(input())
while N < 1 or N > 1000:
    N = int(input())

K = int(input())
while K < 1 or K > N:
    K = int(input())

notas = []
for _ in range(0, N):
    notas.append(int(input()))

notas.sort(reverse = True)

if K == 1:
    if len(notas) > 1:
        contagem = notas.count(max(notas))
    else:
        contagem = 1
else:
    contagem = 0
    for _ in range(1, K):
        notas.pop(0)
        contagem += 1
    valorfinal = notas.count(max(notas))
    contagem += valorfinal

print(contagem)
